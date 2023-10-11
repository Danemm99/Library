from django.contrib import admin
from .models import Author
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id','name','surname']
    sortable_by = ['id', 'surname']
    list_display_links = ['id', 'name', 'surname']

admin.site.register(Author, AuthorAdmin)