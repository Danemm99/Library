from django.contrib import admin
from .models import Order

class AdminOrder(admin.ModelAdmin):
    list_display = ['book', 'user', 'created_at', 'end_at']
    list_filter = ['end_at']
    list_display_links = ['book', 'user']
    fields = ['book', 'user', 'plated_end_at','end_at']

admin.site.register(Order, AdminOrder)