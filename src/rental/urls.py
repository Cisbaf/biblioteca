from django.urls import path
from rental import views


urlpatterns = [
    path('history', views.history, name="history"),
    path('rent/<str:slug>', views.rent_book, name="rent_book"),
    path('devolution/<str:pk>', views.devolution_book, name="devolution_book")
]