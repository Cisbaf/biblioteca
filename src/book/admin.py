from django.contrib import admin
from .models import Book, Category

class AdminCategory(admin.ModelAdmin):
    pass

class AdminBook(admin.ModelAdmin):
    list_display = ['title', 'author', 'instructions', 'get_categories']
    list_filter = ['category']
    search_fields = ['title']  # Habilita o campo de busca no admin

    def get_categories(self, obj):
        return ", ".join([cat.name for cat in obj.category.all()])
    
    get_categories.short_description = 'Categorias'  # Título da coluna no admin


admin.site.register(Book, AdminBook)
admin.site.register(Category, AdminCategory)