from django.contrib import admin
from .models import Ticket


class AdminTicket(admin.ModelAdmin):
    pass


admin.site.register(Ticket, AdminTicket)
# Register your models here.
