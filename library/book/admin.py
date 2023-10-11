from django.contrib import admin
from .models import *

class AdminBook(admin.ModelAdmin):
    list_display = ['id', 'name', 'count']
    list_display_links = ['id', 'name', 'count']
    sortable_by = ['id', 'name', 'count']
    fields = ['name', 'description', 'count', 'authors']
    # list_editable = ['name','count','description']

admin.site.register(Book, AdminBook)