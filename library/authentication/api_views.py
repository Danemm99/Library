# author/api_views.py
from rest_framework import generics
from rest_framework.generics import RetrieveAPIView

from .models import CustomUser
from rest_framework import serializers
from order.models import Order


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class UserOrderCreateAPIView(generics.RetrieveAPIView):
    serializer_class = OrderSerializer
    def get_queryset(self):
        user_id = self.kwargs['user_id']
        print(user_id)
        return Order.objects.filter(user=user_id)

