from django.shortcuts import render, redirect
from .models import Book, Category
from django.db.models import Q
from django.db.models.functions import Lower
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def books(request):
    if not request.user.is_authenticated:
        return redirect("login")
    if request.method == "GET":
        search = request.GET.get('search', None)
        letter = request.GET.get('letter', None)
        category = request.GET.get('category', None)

    filters_used = []
    filters = Q()
    if search:
        search_lower = search.lower()  # Normaliza a entrada do usuário para minúscula
        filters &= (Q(title__icontains=search_lower) | 
                    Q(author__icontains=search_lower) | 
                    Q(description__icontains=search_lower))
        filters_used.append({'name': 'search', 'value': search})

    if letter:
        letter_lower = letter.lower()
        filters &= Q(title__istartswith=letter_lower)
        filters_used.append({'name': 'letter', 'value': letter})

    if category:
        category_lower = category.lower()
        filters &= Q(category__name__iexact=category_lower)  # iexact = insensível a maiúsculas/minúsculas
        filters_used.append({'name': 'category', 'value': category})

    books = Book.objects.annotate(
        title_lower=Lower('title'),
        author_lower=Lower('author'),
        description_lower=Lower('description')
    ).filter(filters).distinct()

    if not len(filters_used):
        page = request.GET.get('page', None)
        paginator = Paginator(books, 10)
        if page:
            books = paginator.page(page)
        else:
            books = paginator.page(1)


    categories = Category.objects.all()
    letter_filter = [chr(i) for i in range(65, 91)]
    context = {
        "letter_filter": letter_filter,
        "books": books,
        "categories": categories,
        "filters_used": filters_used,
    }
    return render(request, "index.html", context=context)

def detail(request, slug):
    book = Book.objects.get(slug=slug)
    context = {
        "book": book
    }
    return render(request, "detail.html", context=context)