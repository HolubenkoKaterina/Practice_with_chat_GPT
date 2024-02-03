### Задача: Поиск простых чисел
# Напишите функцию, которая принимает число `n` и возвращает список всех простых чисел от 2 до `n`.

# def find_primes(n):
#     list_out = []
#     for num in range(2, n + 1):
#         is_prime = True
#         for i in range(2, int(num**0.5) + 1):
#             if num % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             list_out.append(num)
#     return list_out
#
# # Пример использования:
# result = find_primes(20)
# print(result)  # Ожидаемый вывод: [2, 3, 5, 7, 11, 13, 17, 19]


# Простое число - это натуральное число, большее 1, которое не имеет положительных делителей, кроме 1 и самого себя.
# Попробуйте написать функцию для этой задачи. Если у вас есть вопросы или нужна помощь, не стесняйтесь спрашивать!

# def factorial(n):
#     mult = 1
#     if n == 0:
#         return 1
#     if n > 1:
#         for i in range(1, n + 1):
#             mult *= i
#     return mult
#
#
# # Пример использования:
# result = factorial(5)
# print(result)  # Ожидаемый вывод: 120
