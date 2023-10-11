from django.shortcuts import render, redirect
from authentication.models import CustomUser, CustomUserManager

from django.shortcuts import render, redirect, get_object_or_404
from authentication.models import CustomUser

from django.http import HttpResponse
from book.models import Book
from order.models import Order

from datetime import datetime, timedelta

def all_books(request):
    books = Book.objects.all()
    user_id = request.session.get('user_id')
    user = CustomUser.get_by_id(user_id)
    return render(request, 'books/all_books.html', {'books': books, 'librarian': True if user.role == 1 else False})

def view_book(request, book_id):
    book = Book.objects.get(id=book_id)
    user_id = request.session.get('user_id')
    user = CustomUser.get_by_id(user_id)
    return render(request, 'books/view_book.html', {'book': book, 'librarian': True if user.role == 1 else False})


def filter_books(request):
    genre = request.GET.get('genre')
    books = []
    user_id = request.session.get('user_id')
    user = CustomUser.get_by_id(user_id)
    if genre:
        books = Book.objects.filter(description=genre)
    else:
        books = Book.objects.all()

    return render(request, 'books/all_books.html', {'books': books, 'librarian': True if user.role == 1 else False})
