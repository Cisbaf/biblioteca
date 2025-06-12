from django.db import models
from django.contrib.auth.models import User
from book.models import Book
from datetime import date

class ConfigRental(models.Model):
    return_days = models.IntegerField("Tempo de Devolução (dias)", default=30)
    max_books_rented = models.IntegerField("Quantidade Máxima de Livros Alugados", default=3)

    class Meta:
        verbose_name = "Configuração de Aluguel"
        verbose_name_plural = "Configurações de Aluguel"

    def __str__(self):
        return "Regras de Aluguel"

    def save(self, *args, **kwargs):
        if not self.pk and ConfigRental.objects.exists():
            raise Exception("Permitido apenas um registro de configuração!")
        super().save(*args, **kwargs)

class Rental(models.Model):
    book = models.ForeignKey(verbose_name="Livro", to=Book, on_delete=models.CASCADE, related_name="rentals")
    user = models.ForeignKey(verbose_name="Colaborador", to=User, on_delete=models.CASCADE)
    rental_date = models.DateField("Data do Aluguel", auto_now_add=True)
    deadline_date = models.DateField("Data Limite para Devolução", null=True, blank=True)
    return_date = models.DateField("Data de Devolução", null=True, blank=True)
    active = models.BooleanField("Ativo", default=True)

    class Meta:
        verbose_name = "Aluguel de Livro"
        verbose_name_plural = "Aluguéis de Livros"

    @property
    def calendar_days(self):
        return (self.deadline_date - date.today()).days

    def __str__(self):
        return f"Aluguel de {self.book.title} por {self.user.username}"
