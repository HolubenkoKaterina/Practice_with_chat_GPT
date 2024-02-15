# Реализуйте дескриптор LimitedNumber, который ограничит устанавливаемые значения числа в
# определенном диапазоне. При попытке установить значение вне этого
# диапазона, генерируйте исключение ValueError.

# class LimitedNumber:
#     def __init__(self, number, limit_start, limit_end):
#         self.number = None
#         self.limit_start = limit_start
#         self.limit_end = limit_end
#
#     def __set__(self, instance, value):
#         if self.limit_start <= self.number <= self.limit_end:
#             self.number = value
#         else:
#             raise ValueError
#
#     def __get__(self, instance, owner):
#         return self.number
#
# class MyClass:
#     number = LimitedNumber(1, 10)
#
# # Пример использования
# num = MyClass()
# num.number = 5
# print(num.number)  # Вывод: 5

# # Попытка установить значение вне диапазона
# try:
#     num.number = 15
# except ValueError as e:
#     print(f"Ошибка: {e}")



