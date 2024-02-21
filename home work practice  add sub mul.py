# Вам поручается создать программу по учету книг (библиотеку).
# Для этого необходимо в программе объявить два класса:
# Lib - для представления библиотеки в целом;
# Book - для описания отдельной книги.
# Объекты класса Book должны создаваться командой:
# book = Book(title, author, year)
# где title - заголовок книги (строка); author - автор книги (строка); year - год издания (целое число).
# Объекты класса Lib создаются командой:
# lib = Lib()
# Каждый объект должен содержать локальный публичный атрибут:
# book_list - ссылка на список из книг (объектов класса Book).
# Изначально список пустой.

# Также объекты класса Lib должны работать со следующими операторами:
# lib = lib + book # добавление новой книги в библиотеку
# lib += book
# lib = lib - book # удаление книги book из библиотеки (удаление происходит по ранее созданному объекту book класса Book)
# lib -= book
# lib = lib - indx # удаление книги по ее порядковому номеру (индексу: отсчет начинается с нуля)
# lib -= indx
# При реализации бинарных операторов + и - создавать копии библиотек (объекты класса Lib) не нужно.
# Также с объектами класса Lib должна работать функция:
# n = len(lib) # n - число книг
# которая возвращает число книг в библиотеке.

class Lib:
    def __init__(self):
        self.book_list = []

    def __add__(self, other):
        if isinstance(other, Book):
            self.book_list.append(other)
            return self
        raise ValueError('Can`t add not Book objects ')

    def __sub__(self, other):
        if isinstance(other, Book):
            self.book_list.remove(other)
            return self
        raise ValueError('Can`t sub not Book objects ')

    def __str__(self):
        return '\n'.join(str(book) for book in self.book_list)


    def __len__(self):
        return len(self.book_list)

    def delete_on_index(self, index):
        if index < 0 or index >= len(self.book_list):
            raise ValueError('Invalid index!')
        else:
            self.book_list.pop(index)


class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f'{self.title}'





lib = Lib()
book1 = Book('1 book', 'first author', 2024)
book2 = Book('2 book', '2 author', 2023)
book3 = Book('3 book', '3 author', 2022)
book4 = Book('4 book', '4 author', 2021)
lib + book1
lib + book2
lib + book3
lib + book4
# print(lib)
lib.__sub__(book1)
# print(lib)
print(lib.__len__())
lib.delete_on_index(2)
print(lib)

