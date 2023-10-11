from django.urls import path, re_path
from .views import *
urlpatterns = [
    path('', show_all_users, name='all_user'),
    path('profile/<int:user_id>/', show_one_user, name='one_user')

]
