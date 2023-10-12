from django import forms
from book.models import Book

book_names = [(i.id, i.name) for i in Book.objects.all()]
class OrderForm(forms.Form):
    book_name = forms.ChoiceField(choices=book_names)