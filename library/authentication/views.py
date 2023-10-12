# Create your views here.


from django.shortcuts import render, redirect
from . models import CustomUser, CustomUserManager

from django.shortcuts import render, redirect, get_object_or_404
from . models import CustomUser

from django.http import HttpResponse
from book.models import Book


from datetime import datetime, timedelta


def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POST['first_name']
        middle_name = request.POST['middle_name']
        last_name = request.POST['last_name']
        role = int(request.POST.get('role', 0))

        # Перевірка наявності користувача з таким же email
        if CustomUser.objects.filter(email=email).exists():
            return render(request, 'registration/register.html', {'error': 'Акаунт з такою поштою вже існує.'})

        # Створення користувача
        CustomUser.objects.create(email=email, password=password, first_name=first_name, middle_name=middle_name,
                                  last_name=last_name, role=role)
        return redirect('login')

    return render(request, 'registration/register.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = CustomUser.get_by_email(email)
        # Перевірка наявності користувача з таким email та паролем
        if user and user.password == password:
            # Логін користувача
            request.session['user_id'] = user.id
            CustomUser.objects.filter(id=user.id).update(is_active=True)
            return redirect('home')
        else:
            return render(request, 'login/login.html', {'error': 'Невірна пошта або пароль.'})
    return render(request, 'login/login.html')

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
    return render(request, 'main/main.html',context )

# def all_books(request):
#     books = Book.objects.all()
#     return render(request, 'books/all_books.html', {'books': books})
#
# def view_book(request, book_id):
#     book = Book.objects.get(id=book_id)
#     return render(request, 'books/view_book.html', {'book': book})
#
#
# def filter_books(request):
#     genre = request.GET.get('genre')
#     books = []
#     if genre:
#         books = Book.objects.filter(description=genre)
#     else:
#         books = Book.objects.all()
#
#     return render(request, 'books/all_books.html', {'books': books})

# def make_order(request):
#     if request.method == 'POST':
#         name_of_book = request.POST['name']
#
#         if not Book.objects.filter(name=name_of_book).exists():
#             return render(request, 'user_order/user_order.html', {'error': 'Такої книги немає у наявності.'})
#
#         user_id = request.session.get('user_id')
#         book_id = Book.get_by_name(name_of_book).id
#
#         if Order.objects.filter(book_id=book_id, user_id=user_id).exists():
#             return render(request, 'user_order/user_order.html', {'error': 'Таке замовлення вже існує.'})
#
#         # Створення користувача
#         current_datetime = datetime.now()
#         plated_end_at = current_datetime + timedelta(weeks=2)
#         Order.objects.create(book_id=book_id, user_id=user_id, plated_end_at=plated_end_at)
#
#         redirect('make_order')
#
#     return render(request, 'user_order/user_order.html')


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
