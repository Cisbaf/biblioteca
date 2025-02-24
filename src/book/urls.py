from django.urls import path
from book import views



urlpatterns = [
    path('', views.books, name="book"),
    path('<str:slug>', views.detail, name="book_detail")
] 
