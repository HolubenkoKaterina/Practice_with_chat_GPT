# Задача: Дескриптор для ограничения длины строки
# Создайте дескриптор LimitedString, который будет использоваться для хранения строк
# с ограниченной длиной. Дескриптор должен иметь следующее поведение:
# При установке значения (при создании экземпляра класса или
# при присваивании нового значения) проверьте, что длина строки не
# превышает заданного ограничения. Если превышает, выведите сообщение об ошибке.

class LimitedString:
    def __init__(self, max_length):
        self.max_length = max_length
        self._value = None

    def __set__(self, instance, value):
        if len(value) <= self.max_length:
            self._value = value
        else:
            raise ValueError(f"Превышена максимальная длина строки ({self.max_length})")

    def __get__(self, instance, owner):
        return self._value


class User:
    username = LimitedString(10)

    def __init__(self, username):
        self.username = username


# Пример использования
user = User("john_doe")
print(user.username)  # Вывод: john_doe

# Попытка установить слишком длинное имя пользователя
try:
    user.username = "user123456"
except ValueError as e:
    print(f"Ошибка: {e}")
