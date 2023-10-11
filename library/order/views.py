from django.shortcuts import render, redirect
from authentication.models import CustomUser, CustomUserManager

from django.shortcuts import render, redirect, get_object_or_404
from authentication.models import CustomUser

from django.http import HttpResponse
from book.models import Book
from order.models import Order

from datetime import datetime, timedelta
def make_order(request):
    if request.method == 'POST':
        name_of_book = request.POST['name']

        if not Book.objects.filter(name=name_of_book).exists():
            return render(request, 'user_order/user_order.html', {'error': 'Такої книги немає у наявності.'})

        user_id = request.session.get('user_id')
        book_id = Book.get_by_name(name_of_book).id

        if Order.objects.filter(book_id=book_id, user_id=user_id).exists():
            return render(request, 'user_order/user_order.html', {'error': 'Таке замовлення вже існує.'})

        # Створення користувача
        current_datetime = datetime.now()
        plated_end_at = current_datetime + timedelta(weeks=2)
        Order.objects.create(book_id=book_id, user_id=user_id, plated_end_at=plated_end_at)

        redirect('make_order')

    return render(request, 'user_order/user_order.html')


def show_orders(request):
    user_id = request.session.get('user_id')
    user = CustomUser.get_by_id(user_id)
    if user.role == 0:
        orders = Order.objects.filter(user=user_id)
        book_ids = [order.book_id for order in orders]

        # Отримуємо книги за відповідними id та формуємо словник
        books_info = [{'name': book.name, 'description': book.description} for book in Book.objects.filter(id__in=book_ids)]
        print(books_info)

        context = {'books': books_info}  # Створюємо контекст із словником книг
        return render(request, 'my_order/orders_list.html', context)

    else:
        return HttpResponse('<p>You have no rights</p>')
def all_orders(request):
    user_id = request.session.get('user_id')
    user = CustomUser.get_by_id(user_id)
    if user.role == 1:
        context = {
            'orders': Order.objects.all(),
            'librarian': True
        }
        return render(request, 'order/all_orders.html', context)
    else:
        return HttpResponse('<p>You have no rights</p>')

def done_order(request, order_id):
    user_id = request.session.get('user_id')
    user = CustomUser.get_by_id(user_id)
    if user.role == 1:
        order = Order.objects.get(id=order_id).update(end_at=datetime.now())
        return redirect('all_orders')
    else:
        return HttpResponse('<p>You have no rights</p>')

