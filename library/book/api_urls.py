from django.urls import path
from . import api_views

urlpatterns = [
    path('api/v1/book/', api_views.BookListCreateAPIView.as_view(), name='book-list-create'),
    path('api/v1/book/<int:pk>/', api_views.BookRetrieveUpdateDestroyAPIView.as_view(), name='book-detail'),
]
