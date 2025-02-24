from django.contrib import admin
from .models import Rental, ConfigRental

# Register your models here.
class AdminRental(admin.ModelAdmin):
    pass


class AdminConfigRental(admin.ModelAdmin):
    pass


admin.site.register(Rental, AdminRental)
admin.site.register(ConfigRental, AdminConfigRental)