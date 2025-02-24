# Generated by Django 5.1.6 on 2025-02-12 12:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_remove_book_available'),
        ('rental', '0002_configrental'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='configrental',
            name='max_books_rented',
            field=models.IntegerField(default=3, verbose_name='Quantidade máxima de livros alugados'),
        ),
        migrations.AlterField(
            model_name='configrental',
            name='return_days',
            field=models.IntegerField(default=30, verbose_name='Tempo de devolução'),
        ),
        migrations.AlterField(
            model_name='rental',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rentals', to='book.book', verbose_name='Livro'),
        ),
        migrations.AlterField(
            model_name='rental',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Colaborador'),
        ),
    ]
