
from django.db import models
from django.contrib.auth.models import User
from book.models import Book
from datetime import date, timedelta

class ConfigRental(models.Model):
    return_days = models.IntegerField(verbose_name="Tempo de devolução", default=30)
    max_books_rented = models.IntegerField(verbose_name="Quantidade máxima de livros alugados", default=3)

    def __str__(self):
        return f"Regras Alugueis"
    
    def save(self, *args, **kwargs):
        if not self.pk and ConfigRental.objects.count():
            raise Exception("Permitido apenas um registro de configuração!")
        super().save(*args, **kwargs)

class Rental(models.Model):
    book = models.ForeignKey(verbose_name="Livro", to=Book, on_delete=models.CASCADE, related_name="rentals")
    user = models.ForeignKey(verbose_name="Colaborador", to=User, on_delete=models.CASCADE)
    rental_date = models.DateField(auto_now_add=True)
    deadline_date = models.DateField(null=True, blank=True)
    return_date = models.DateField(null=True, blank=True)
    active = models.BooleanField(default=True)

    @property
    def calendar_days(self):
        return (self.deadline_date - date.today()).days

        
    
    def __str__(self):
        return f"Rental of {self.book.title} by {self.user.username}"
