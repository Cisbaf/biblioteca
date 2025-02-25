from django.urls import path
from . import views

urlpatterns = [
    # path('', views.ticket_list, name='ticket_list'),
    path('new/', views.ticket_create, name='ticket_create'),
    path('book/<int:pk>', views.ticket_create_book, name="ticket_create_book")
    # path('<int:ticket_id>/edit/', views.ticket_update, name='ticket_update'),
    # path('<int:ticket_id>/delete/', views.ticket_delete, name='ticket_delete'),
]
