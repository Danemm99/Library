from book.models import Book
# from author.models import Author

print(Book.objects.all())

# # Create and save 20 different Book instances
# books_data = [
#     {'id': 1, 'name': 'Book 1', 'description': 'Description 1', 'count': 5},
#     {'id': 2, 'name': 'Book 2', 'description': 'Description 2', 'count': 3},
#     {'id': 3, 'name': 'Book 3', 'description': 'Description 3', 'count': 8},
#     {'id': 4, 'name': 'Book 4', 'description': 'Description 4', 'count': 10},
#     {'id': 5, 'name': 'Book 5', 'description': 'Description 5', 'count': 12},
#     {'id': 6, 'name': 'Book 6', 'description': 'Description 6', 'count': 7},
#     {'id': 7, 'name': 'Book 7', 'description': 'Description 7', 'count': 4},
#     {'id': 8, 'name': 'Book 8', 'description': 'Description 8', 'count': 9},
#     {'id': 9, 'name': 'Book 9', 'description': 'Description 9', 'count': 6},
#     {'id': 10, 'name': 'Book 10', 'description': 'Description 10', 'count': 11},
#     {'id': 11, 'name': 'Book 11', 'description': 'Description 11', 'count': 2},
#     {'id': 12, 'name': 'Book 12', 'description': 'Description 12', 'count': 15},
#     {'id': 13, 'name': 'Book 13', 'description': 'Description 13', 'count': 14},
#     {'id': 14, 'name': 'Book 14', 'description': 'Description 14', 'count': 7},
#     {'id': 15, 'name': 'Book 15', 'description': 'Description 15', 'count': 3},
#     {'id': 16, 'name': 'Book 16', 'description': 'Description 16', 'count': 6},
#     {'id': 17, 'name': 'Book 17', 'description': 'Description 17', 'count': 8},
#     {'id': 18, 'name': 'Book 18', 'description': 'Description 18', 'count': 9},
#     {'id': 19, 'name': 'Book 19', 'description': 'Description 19', 'count': 4},
#     {'id': 20, 'name': 'Book 20', 'description': 'Description 20', 'count': 13},
# ]
# books = []
# for book_data in books_data:
#     book = Book(**book_data)
#     book.save()
#     books.append(book)
#
# authors_data = [
#     {'id': 11, 'name': 'John', 'surname': 'Doe', 'patronymic': 'Smith'},
#     {'id': 12, 'name': 'Alice', 'surname': 'Johnson', 'patronymic': 'Brown'},
#     {'id': 13, 'name': 'Michael', 'surname': 'Williams', 'patronymic': 'Lee'},
#     {'id': 14, 'name': 'Emily', 'surname': 'Wilson', 'patronymic': 'Clark'},
#     {'id': 15, 'name': 'James', 'surname': 'Anderson', 'patronymic': 'White'},
#     {'id': 16, 'name': 'Sophia', 'surname': 'Martin', 'patronymic': 'Taylor'},
#     {'id': 17, 'name': 'Daniel', 'surname': 'Garcia', 'patronymic': 'Davis'},
#     {'id': 18, 'name': 'Olivia', 'surname': 'Hernandez', 'patronymic': 'Johnson'},
#     {'id': 19, 'name': 'William', 'surname': 'Lewis', 'patronymic': 'Moore'},
#     {'id': 20, 'name': 'Emma', 'surname': 'Brown', 'patronymic': 'Adams'},
# ]
#
# for author_data in authors_data:
#     author = Author(**author_data)
#     author.save()