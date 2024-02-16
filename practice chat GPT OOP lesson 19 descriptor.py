# Напишите класс Book, который будет использован
# для представления информации о книгах.
# Каждая книга должна иметь атрибуты title(название), author(автор),
# pages(количество страниц) и weight(вес книги).
# Стол WeightDescriptor необходимо проверить, что масса книги
# находится в допустимом соотношении от 100 до 1000 грамм.
# Если значение веса не входит в этот диапазон,
# необходимо вызвать исключение ValueError.
class WeightDescriptor:
    def __init__(self, min_weight, max_weight):
        self.min_weight = min_weight
        self.max_weight = max_weight

    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if instance(value, (int, float)) and self.min_weight <= Book.weigh >= self.max_weight:
            setattr(instance, self.name, value)
        else:
            raise ValueError

    def __get__(self, instance, owner):
        return getattr(instance, self.name)



class Book:
    weigh = WeightDescriptor(100, 1000)
    def __init__(self, title, author, pages, weight):
        self.author = author
        self.title = title
        self.pages = pages
        self.weight = weight


    def get_book(self):
        return f'название {self.title} автор {self.author}'
# Пример использования:
book = Book("1984", "George Orwell", 328, 500)
print(book.weight)  # Ожидаемый вывод: 500
book.weight = 1200  # Вызов исключения ValueError
