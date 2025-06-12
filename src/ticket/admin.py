from django.contrib import admin
from .models import Ticket


class AdminTicket(admin.ModelAdmin):
    list_display = ['book__title', 'title', 'description', 'user__username', 'created_at']


admin.site.register(Ticket, AdminTicket)
# Register your models here.
