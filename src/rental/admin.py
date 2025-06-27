from django.contrib import admin
from .models import Rental, ConfigRental

class DevolvidoFilter(admin.SimpleListFilter):
    title = 'Devolvido'
    parameter_name = 'devolvido'

    def lookups(self, request, model_admin):
        return [
            ('sim', 'Sim'),
            ('nao', 'Não'),
        ]

    def queryset(self, request, queryset):
        if self.value() == 'sim':
            return queryset.exclude(return_date__isnull=True)
        if self.value() == 'nao':
            return queryset.filter(return_date__isnull=True)
        return queryset

class AdminRental(admin.ModelAdmin):
    list_display = [
        'get_title',
        'get_full_name',
        'user__email',
        'get_rental_date',
        'deadline_date',
        'return_date',
        'get_status',
        'get_devolution'
    ]
    list_filter = [DevolvidoFilter]
    search_fields = ['book__title', 'user__first_name']

    @admin.display(description="Titulo do livro")
    def get_title(self, obj):
        return obj.book.title

    @admin.display(description="Solicitante")
    def get_full_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"

    @admin.display(description="Data realização do empréstimo")
    def get_rental_date(self, obj):
        return obj.rental_date

    @admin.display(description="Status do Empréstimo")
    def get_status(self, obj):
        return obj.status_time()

    @admin.display(description="Devolvido?", boolean=True)
    def get_devolution(self, obj):
        return obj.return_date is not None

class AdminConfigRental(admin.ModelAdmin):
    pass

admin.site.register(Rental, AdminRental)
admin.site.register(ConfigRental, AdminConfigRental)
