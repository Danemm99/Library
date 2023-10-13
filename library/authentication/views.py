from django.shortcuts import render, redirect
from . models import CustomUser, CustomUserManager

from django.shortcuts import render, redirect, get_object_or_404
from . models import CustomUser

from django.http import HttpResponse
from book.models import Book


from datetime import datetime, timedelta

from .forms import RegistrationForm, LoginForm


# def register(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']
#         first_name = request.POST['first_name']
#         middle_name = request.POST['middle_name']
#         last_name = request.POST['last_name']
#         role = int(request.POST.get('role', 0))
#
#         # Перевірка наявності користувача з таким же email
#         if CustomUser.objects.filter(email=email).exists():
#             return render(request, 'registration/register.html', {'error': 'Акаунт з такою поштою вже існує.'})
#
#         # Створення користувача
#         if role == 0:
#             user = CustomUser.objects.create(email=email, password=password, first_name=first_name, middle_name=middle_name,
#                                   last_name=last_name, role=role)
#             user.set_password(password)
#             user.save()
#
#         elif role == 1:
#             user = CustomUser.objects.create(email=email, password=password, first_name=first_name, middle_name=middle_name,
#                                       last_name=last_name, role=role, is_staff=True, is_superuser=True)
#             user.set_password(password)
#             user.save()
#
#         return redirect('login')
#
#     return render(request, 'registration/register.html')
#
# def login_view(request):
#     if CustomUser.objects.filter(is_active=True).exists():
#         return redirect('home')
#
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']
#         user = CustomUser.get_by_email(email)
#         # Перевірка наявності користувача з таким email та паролем
#         if user and user.password == password:
#             # Логін користувача
#             request.session['user_id'] = user.id
#             CustomUser.objects.filter(id=user.id).update(is_active=True)
#             return redirect('home')
#         else:
#             return render(request, 'login/login.html', {'error': 'Невірна пошта або пароль.'})
#     return render(request, 'login/login.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if CustomUser.objects.filter(is_active=True).exists():
        return redirect('home')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = CustomUser.get_by_email(email)
            if user and user.password == password:
                request.session['user_id'] = user.id
                CustomUser.objects.filter(id=user.id).update(is_active=True)
                return redirect('home')
            else:
                return render(request, 'login/login.html', {'form': form, 'error': 'Невірна пошта або пароль.'})
    else:
        form = LoginForm()
    return render(request, 'login/login.html', {'form': form})

def logout_view(request):
     if 'user_id' in request.session:
         user_id = request.session.get('user_id')
         CustomUser.objects.filter(id=user_id).update(is_active=False)
         del request.session['user_id']
     return redirect('main')

def home(request):
    # Отримання ID користувача з сесії (якщо користувач увійшов в систему)
    user_id = request.session.get('user_id')
    role = CustomUser.get_by_id(user_id).role
    context = {}

    if user_id:
        # Отримання об'єкта користувача за його ID
        user = CustomUser.get_by_id(user_id)
        context['user'] = user
        context['librarian'] = True

    if role == 0:
        return render(request, 'user/user.html', context)

    else:
        return render(request, 'librarian/librarian.html', context)

def main(request):
    user_id = request.session.get('user_id')
    user = CustomUser.get_by_id(user_id)
    if user:
        context = {'librarian': True if user.role == 1 else False}
    else:
        context = {'librarian': False}
    return render(request, 'main/main.html', context)

def show_all_users(request):
    user_id = request.session.get('user_id')
    user = CustomUser.get_by_id(user_id)
    cont = {
        'users': CustomUser.objects.all(),
        'librarian': True if user.role == 1 else False
    }
    return render(request, 'users/all_users.html', context=cont)


def show_one_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    user_id = request.session.get('user_id')
    user_r = CustomUser.get_by_id(user_id)
    context = {
        'user': user,
        'librarian': True if user_r.role == 1 else False
    }
    return render(request, 'users/user_info.html', context)
