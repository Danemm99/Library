from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home, name='home'),
    # path('home/books/', views.all_books, name='books'),
    # path('home/books/<int:book_id>/', views.view_book, name='view_book'),
    # path('home/books/filter_books/', views.filter_books, name='filter_books'),
    # path('home/make_order/', views.make_order, name='make_order'),
    # path('home/books/', views.all_books, name='books'),
    # path('home/books/<int:book_id>/', views.view_book, name='view_book'),
    # path('home/books/filter_books/', views.filter_books, name='filter_books'),
    # path('make_order', views.make_order, name='make_order'),
]
