# Задача: Класс Книжная Библиотека
# Создайте два класса: Book и Library. Каждая книга (Book)
# должна иметь атрибуты: название (title), автор (author),
# год издания (year) и статус доступности (available).
# Book:
# Метод __init__: инициализирует атрибуты книги при создании объекта.
# Метод display_info: выводит информацию о книге в формате "Название, Автор, Год издания".
# Метод checkin: изменяет статус доступности книги на "доступна".
# Метод checkout: изменяет статус доступности книги на "недоступна".
# Library:
# Метод __init__: инициализирует атрибут библиотеки при
# создании объекта. Библиотека должна содержать список книг.
# Метод add_book: добавляет новую книгу в библиотеку.
# Метод find_book: находит книгу по названию и выводит ее информацию.
# Метод display_books: выводит информацию о всех книгах в библиотеке.
# class Book:
#     def __init__(self, title, author, year, available=True):
#         self.title = title
#         self.author = author
#         self.year = year
#         self.available = available
#
#     def display_info(self):
#         print(f'Название {self.title}, Автор {self.author}, Год издания {self.year}')
#
#     def checkin(self):
#        self.available = True
#
#     def checkout(self):
#         self.available = False
#
# class Library:
#     def __init__(self):
#         self.book_list = []
#
#     def add_book(self, book):
#         self.book_list.append(book)
#
#     def find_book(self, title):
#         for book in self.book_list:
#             if book.title == title:
#                 return book
#         return None
#
#     def display_books(self):
#         for book in self.book_list:
#             print(f'Название: {book.title}, Автор: {book.author}, Год издания: {book.year}, Доступна: {book.available}')
#
# # Создаем объекты книг
# book1 = Book("Python без проблем", "Даниэль Зингаро", 2020)
# book2 = Book("Грокаем алгоритмы", "Адитья Бхаргава", 2005)
# # Создаем библиотеку
# library = Library()
# # Добавляем книги в библиотеку
# library.add_book(book1)
# library.add_book(book2)
# # Пытаемся найти книгу по названию
# found_book = library.find_book("Python без проблем")
# # Выводим результат
# if found_book:
#     print(f'Книга найдена: {found_book.title}')
# else:
#     print("Книга не найдена")