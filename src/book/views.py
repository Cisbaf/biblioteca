from django.shortcuts import render
from .models import Book, Category
from django.db.models import Q
from django.db.models.functions import Lower
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from django.db.models import Q, Count, Case, When, Value, IntegerField
from django.db.models.functions import Lower
from django.core.paginator import Paginator

@login_required(login_url='login')
def books(request):
    search = request.GET.get('search', None)
    letter = request.GET.get('letter', None)
    category = request.GET.get('category', None)

    filters_used = []
    filters = Q()
    
    if search:
        search_lower = search.lower()
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
        filters &= Q(category__name__iexact=category_lower)
        filters_used.append({'name': 'category', 'value': category})

    books_qs = Book.objects.annotate(
        title_lower=Lower('title'),
        author_lower=Lower('author'),
        description_lower=Lower('description')
    ).filter(filters).distinct()

    # Se não houver filtro, aplicar recomendação
    if not filters_used:
        books_qs = books_qs.annotate(
            total_rentals=Count('rentals'),
            is_rented=Case(
                When(rentals__active=True, then=Value(1)),
                default=Value(0),
                output_field=IntegerField()
            )
        ).order_by('is_rented', '-total_rentals')

    # Paginação
    page = request.GET.get('page', 1)
    paginator = Paginator(books_qs, 9)
    books = paginator.get_page(page)

    categories = Category.objects.all()
    letter_filter = [chr(i) for i in range(65, 91)]

    context = {
        "letter_filter": letter_filter,
        "books": books,
        "categories": categories,
        "filters_used": filters_used,
    }
    return render(request, "index.html", context=context)

@login_required(login_url='login')
def detail(request, slug):
    book = Book.objects.get(slug=slug)
    context = {
        "book": book
    }
    return render(request, "detail.html", context=context)