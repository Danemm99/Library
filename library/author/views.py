# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Author
from authentication.models import CustomUser
from .forms import *

def show_all_authors(request):
    user_id = request.session.get('user_id')
    user = CustomUser.get_by_id(user_id)
    if user.role == 1:
        context = {
            'authors': Author.objects.all(),
            "librarian": True,
        }
        return render(request, "author/all_authors.html", context)
    else:
        return HttpResponse('<h3>You have no rigths<h3>' + str(CustomUser.role))

def show_one_author(request, author_id):
    user_id = request.session.get('user_id')
    user = CustomUser.get_by_id(user_id)
    if user.role == 1:
        context = {
            'author': Author.objects.get(id=author_id),
            'books': Author.objects.get(id=author_id).books.all(),
            "librarian": True
        }
        return render(request, 'author/one_author.html', context)
    else:
        return HttpResponse('<h3>You have no rigths<h3>')


def delete_author(request, author_id):
    user_id = request.session.get('user_id')
    user = CustomUser.get_by_id(user_id)
    if user.role == 1:
        Author.delete_by_id(author_id)
        return redirect('all_authors')
    else:
        return HttpResponse('<h3>You have no rigths<h3>')


def add_author_page(request):
    user_id = request.session.get('user_id')
    user = CustomUser.get_by_id(user_id)
    if user.role == 1:
        if request.method == 'POST':
            form = AuthorForm(request.POST)
            if form.is_valid():
                u = form.save()
                return redirect('all_authors')
        else:
            form_class = AuthorForm
            return render(request, 'author/add_author.html', context={"librarian":True, 'form': form_class})
    else:
        HttpResponse("<h1>You have no rights</h1>")


