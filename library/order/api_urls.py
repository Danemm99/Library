# order/urls.py
from django.urls import path
from . import api_views

urlpatterns = [
    path('api/v1/order/', api_views.OrderListCreateAPIView.as_view(), name='order-list-create'),
    path('api/v1/order/<int:pk>/', api_views.OrderRetrieveUpdateDestroyAPIView.as_view(), name='order-detail'),
]
