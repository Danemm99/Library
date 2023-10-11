from django.urls import path
from . import views

urlpatterns = [
    path('home/books/', views.all_books, name='books'),
    path('home/books/<int:book_id>/', views.view_book, name='view_book'),
    path('home/books/filter_books/', views.filter_books, name='filter_books'),
]
