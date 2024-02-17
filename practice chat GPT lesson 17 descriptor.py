# Реализовать дескриптор LimitedString, который сокращает длину строк в атрибуте класса.
# Создайте класс LimitedString, у которого есть атрибут max_length- наибольшая длина строки.
# Реализуйте метод __set__, который при установке значения будет проверять
# его тип (должен быть строкой) и длину. Если увеличить длину max_length,
# сгенерируйте вывод ValueError с сообщением «Превышена максимальная длина строки».
# В противном случае установите значение.
# Реализуйте метод __get__, который возвращает значение атрибута.

class LimitedString:
    def __init__(self, max_length):
        self.__max_length = max_length
        self.string = None

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError('Значение должно быть строкой')
        if len(value) > self.__max_length:
            raise ValueError('Превышена максимальная длина строки')
        else:
            self.string = value

    def __get__(self, instance, owner):
        return self.string

    def __str__(self):
        return f'{self.string} {self.__max_length}'

class User:
    leng = LimitedString(4)

    def __init__(self, string):
        self.leng = string  # Обращаемся к атрибуту leng, а не string

#user = User('i like python')
user = User('like')
print(user.leng)  # Ожидаемый вывод: i like python
