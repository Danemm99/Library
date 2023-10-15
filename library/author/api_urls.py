# author/urls.py
from django.urls import path
from . import api_views

urlpatterns = [
    path('api/v1/author/', api_views.AuthorListCreateAPIView.as_view(), name='author-list-create'),
    path('api/v1/author/<int:pk>/', api_views.AuthorRetrieveUpdateDestroyAPIView.as_view(), name='author-detail'),
]
