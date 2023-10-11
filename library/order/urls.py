from django.urls import path
from . import views

urlpatterns = [
    path('home/make_order/', views.make_order, name='make_order'),
    path('home/my_order/', views.show_orders, name='show_orders'),
    path('all_orders', views.all_orders, name='all_orders'),
    path('done_order/<int:order_id>', views.done_order, name='done_order'),

]
