# Представьте, что вы создаете программу для управления библиотекой.
# Необходимо реализовать класс Library, который будет хранить книги.
# Требования:
# Создайте класс Book, описывающий книгу.
# Каждая книга должна содержать название, автора и жанр.
# Реализуйте класс Library, который будет хранить список книг.
# Library должен иметь методы:
# add_book(book): добавляет книгу в библиотеку.
# remove_book(book_title): удаляет книгу из библиотеки по названию.
# search_by_author(author_name): ищет книги
# по имени автора и возвращает список найденных книг.
# search_by_genre(genre): ищет книги по жанру
# и возвращает список найденных книг.
# get_books_info(): возвращает информацию о
# всех книгах в библиотеке.
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, title):
        for book in self.books:
            if book != title:
                self.books.remove(title)


    def search_by_author(self, author_name):
        found_books = []
        for book in self.books:
            if book.author == author_name:
                found_books.append(book)
                return f'{book}'
            if not found_books:
                raise ValueError('книги с таким автором не найдены!')
            return found_books

    def get_books_info(self):
        return f'{self.books}'

    def search_by_genre(self, genre):
        for book in self.books:
            if book.genre == genre:
                return f'{book}'
        else:
            raise ValueError('книги с таким автором не найдены!')

class Book:
    def __init__(self, title, author, genre):
        self.title = title.title()
        self.author = author.title()
        self.genre = genre

    @property
    def get_name(self):
        return self.title

    @property
    def get_author(self):
        return self.author

    @property
    def get_genre(self):
        return self.genre

    def __str__(self):
        return f'название {self.title} автор {self.author} жанр {self.genre}'

book1 = Book('python для чайников', "пол берри", "учебная")
book2 = Book('алгоритмы ', "дхаварги", "учебная")
book3 = Book('python это просто ', "кори альтхофф", "учебная")
my_library = Library()
my_library.add_book(book1)
my_library.add_book(book2)
my_library.add_book(book3)
my_library.remove_book('python')
my_library.search_by_genre('учебная')
print(my_library)

