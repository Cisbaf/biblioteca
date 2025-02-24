from django.contrib import admin
from .models import Book, Category

class AdminCategory(admin.ModelAdmin):
    pass

class AdminBook(admin.ModelAdmin):
    list_filter = ['category']

admin.site.register(Book, AdminBook)
admin.site.register(Category, AdminCategory)