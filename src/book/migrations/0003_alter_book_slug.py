# Generated by Django 5.1.6 on 2025-02-12 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_book_slug_alter_book_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(blank=True, max_length=200),
        ),
    ]
