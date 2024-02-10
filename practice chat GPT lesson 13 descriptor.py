# Создайте дескриптор cccc,
# который будет использоваться для хранения строк фиксированной длины.
# Длину строки нужно задать при создании экземпляра дескриптора.
# При установке нового значения через дескриптор нужно проверять,
# что длина строки соответствует установленному ограничению.
# Если длина строки больше установленной,
# генерируйте исключение ValueError с сообщением "Превышена максимальная длина строки".
class LimitedString:
    def __init__(self, max_length, default_value=''):
        self.max_length = max_length
        self.default_value = default_value
        self.my_string = None

    def __set__(self, instance, value):
        if len(value) <= self.max_length:
            self.my_string = value
        else:
            raise ValueError("Превышена максимальная длина строки")

    def __get__(self, instance, owner):
        if self.my_string is not None:
            return self.my_string
        else:
            return self.default_value


# Пример использования
class MyClass:
    name = LimitedString(5, 'Default')

obj = MyClass()

# Попытка установить корректное значение
obj.name = "Hello"
print(obj.name)  # Вывод: Hello

# Попытка установить слишком длинное значение
try:
    obj.name = "World123"
except ValueError as e:
    print(e)  # Вывод: Превышена максимальная длина строки

# Если не устанавливать явно, будет использовано значение по умолчанию
print(obj.name)  # Вывод: Default




