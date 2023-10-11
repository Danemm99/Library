from django.urls import path

from .views import *

urlpatterns = [
    path('', show_all_authors, name='all_authors'),
    path('author/<int:author_id>', show_one_author, name='author_info'),
    path('delete_author/<int:author_id>', delete_author, name='delete_author'),
    path('add_author_page', add_author_page, name='add_author_page'),
]
