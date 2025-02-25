from django.shortcuts import render, redirect
from app.helper.http import previus
from .models import Ticket, Book
from django.contrib import messages


def ticket_create(request):
    if request.method == 'POST':
        pass

    return redirect(previus(request))
    
def ticket_create_book(request, pk):
    if request.method == 'POST':
        title = request.POST.get("title")
        description = request.POST.get("description")
        Ticket.objects.create(
            title=title,
            description=description,
            book=Book.objects.get(id=pk),
            user=request.user
        )
        messages.success(request, "Ticket Aberto com sucesso!")

    return redirect(previus(request, '/'))
    