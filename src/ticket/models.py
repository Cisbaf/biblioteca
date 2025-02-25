from django.db import models
from django.contrib.auth.models import User
from book.models import Book


class Ticket(models.Model):
    STATUS_CHOICES = [
        ('open', 'Aberto'),
        ('in_progress', 'Em Progresso'),
        ('closed', 'Fechado'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    book = models.ForeignKey(to=Book, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title