from django.contrib import admin
from .models import CustomUser


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'last_name', 'first_name', 'email']
    list_filter = ['created_at']
    fields = [('last_name', 'first_name', 'middle_name'), 'email', 'role', 'password']
    sortable_by = ['id', 'last_name']
    list_display_links = ['id', 'email', 'last_name','first_name']

admin.site.register(CustomUser, UserAdmin)





