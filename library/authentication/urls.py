from django.urls import path
from . import views, api_views

urlpatterns = [
    path('', views.main, name='main'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home, name='home'),
#API urls
    path('api/v1/user/', api_views.UserListCreateAPIView.as_view(), name='user-list-create'),
    path('api/v1/user/<int:pk>/', api_views.UserRetrieveUpdateDestroyAPIView.as_view(), name='user-detail'),
    path('api/v1/user/<int:user_id>/order/<int:pk>', api_views.UserOrderCreateAPIView.as_view(), name='user-order-create'),
]

