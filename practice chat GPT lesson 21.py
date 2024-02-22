# # Задача: Электронная библиотека
# # Разработайте программу для управления электронной библиотекой. В системе должны быть следующие классы:
# #
# # Книга (Book):
# #
# # Свойства: Название, Автор, Год издания, ISBN (уникальный идентификатор), Количество страниц.
# # Методы: Вывод информации о книге.
# # Библиотека (Library):
# #
# # Свойства: Список книг.
# # Методы: Добавление книги, Удаление книги, Поиск книги по названию или автору, Вывод списка всех книг.
# # Напишите пример использования этих классов, включая создание нескольких книг, их добавление в библиотеку, поиск книг и вывод списка всех книг.
#
# class Book:
#     def __init__(self, title, author, year, ISBN, pages):
#         self.title = title
#         self.author = author
#         self.year = year
#         self.ISBN = ISBN
#         self.pages = pages
#
#     def get_info(self):
#         return f'название: {self.title}\nавтор: {self.author}\nгод издания {self.year}\nкод {self.ISBN}\nкол-во страниц {self.pages}'
#
#
# class Library:
#     def __init__(self):
#         self.books_list = []
#
#     def add_book(self, book):
#         self.books_list.append(book)
#
#     def remove_book(self, book):
#         self.books_list.remove(book)
#
#     def get_library(self):
#         return self.books_list
#
#     def find_book(self, title):
#         find_books = []
#         for book in self.books_list:
#             if title.lower() in book.title.lower():
#                 return find_books
#
#     def find_author(self, author):
#         author_books = []
#         for book in self.books_list:
#             if author.lower() in book.author.lower():
#                 return author_books
#
#
#
#
# book_data_1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, "9780141182636", 218)
# book_data_2 = Book("To Kill a Mockingbird", "Harper Lee", 1960, "0061120081", 324)
# book_data_3 = Book("1984", "George Orwell", 1949, "9780451524935", 328)
# book_data_4 = Book("Pride and Prejudice", "Jane Austen", 1813, "9780141199073", 432)
# book_data_5 = Book("The Catcher in the Rye", "J.D. Salinger", 1951, "9780241950425", 224)
# print(book_data_5.get_info())
# my_library = Library()
# my_library.add_book(book_data_1)
# my_library.add_book(book_data_2)
# my_library.add_book(book_data_3)
# my_library.add_book(book_data_4)
# my_library.add_book(book_data_5)
#
# found_books = my_library.find_book("gatsb")
# print("Books found by title:")
# for book in found_books:
#     print(book.get_info())
#
# found_author_books = my_library.find_author("scott")
# print("Books found by author:")
# for book in found_author_books:
#     print(book.get_info())