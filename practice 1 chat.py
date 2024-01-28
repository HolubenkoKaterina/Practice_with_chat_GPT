### Задача 1: Палиндром
# Напишите функцию, которая проверяет, является ли строка палиндромом.
# Палиндром - это строка, которая читается одинаково вперед и назад, игнорируя пробелы, знаки препинания и регистр.

# def is_palindrome(s):
#     new_s = s.lower().strip().replace(' ', '')
#     if new_s == new_s[::-1]:
#         return True
#     return False
# Пример использования:
# print(is_palindrome("А роза упала на лапу Азора"))  # True
# print(is_palindrome("Python"))  # False

# ### Задача 2: Сумма чисел в диапазоне
# Напишите функцию, которая вычисляет сумму всех целых чисел в заданном диапазоне.
# def sum_in_range(start, end):
#     summa = 0
#     for num in range(start, end +1):
#         summa += num
#     return summa
#
# # Пример использования:
# # print(sum_in_range(1, 10))  # 55
# print(sum_in_range(2, 6))  # 0

# ### Задача 3: Факториал
# Напишите функцию для вычисления факториала числа.
# def factorial(n):
#     factorial = 1
#     if n > 0:
#         for num in range(1, n+1):
#             factorial *= num
#         return factorial
#     else:
#         return 1
#
#
#
# # Пример использования:
# print(factorial(5))  # 120
# print(factorial(0))  # 1
# print(factorial(10))
