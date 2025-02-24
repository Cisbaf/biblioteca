from django.shortcuts import render, redirect
from .models import Rental, Book, ConfigRental
from app.helper.http import previus
from datetime import date, timedelta
from django.contrib import messages


def history(request):
    my_rentals = Rental.objects.filter(user=request.user).order_by("-pk")
    context = {
        "rentals": my_rentals
    }
    return render(request, "rental_history.html", context=context)

def rent_book(request, slug):
    config = ConfigRental.objects.first()
    book = Book.objects.get(slug=slug)
    if (len(Rental.objects.filter(user=request.user, active=True)) >= config.max_books_rented):
        messages.error(request, "Você já tem 3 livros alugados!")
    elif (Rental.objects.filter(book=book, active=True)):
        messages.error(request, "O livro já está alugado!")
    else:
        Rental.objects.create(
            book=book,
            user=request.user,
            deadline_date=date.today()+timedelta(days=config.return_days)
        )
        messages.success(request, f"Livro alugado com sucesso! ({book.title})")
    return redirect(previus(request, '/'))

def devolution_book(request, pk):
    rental = Rental.objects.get(pk=pk)
    rental.active = False
    rental.return_date = date.today()
    rental.save()
    messages.success(request, f"Devolução marcada com sucesso! ({rental.book.title})")
    return redirect(previus(request, '/'))

