from django.contrib import admin
from .models import Rental, ConfigRental

class AdminRental(admin.ModelAdmin):
    list_display = ['book__title', 'user__first_name', 'user__email', 'rental_date', 'deadline_date', 'return_date', 'active']
    list_filter = ['active']
    search_fields = ['book__title', 'user__first_name']

class AdminConfigRental(admin.ModelAdmin):
    pass


admin.site.register(Rental, AdminRental)
admin.site.register(ConfigRental, AdminConfigRental)