# Задача: Анализ оценок студентов
#
# У вас есть данные о результатах экзаменов студентов в виде списка кортежей,
# где каждый кортеж содержит имя студента и их оценку за экзамен.
# Вам нужно написать программу на Python, которая проанализирует эти данные и выполнит следующие действия:
#
# Найдите студента с наивысшей оценкой и выведите его имя и оценку.
# Найдите студента с наименьшей оценкой и выведите его имя и оценку.
# Рассчитайте средний балл всех студентов.
# Определите количество студентов, сдавших экзамен с оценкой выше 90.
# students = [
#     ("Алексей", 85),
#     ("Мария", 90),
#     ("Иван", 75),
#     ("Екатерина", 95),
#     ("Павел", 88)
# ]
# def find_info(some_list: list):
#     total_grade = 0
#     max_grade = float('-inf')
#     min_grade = float('inf')
#     students_over_some_grade = []
#
#     for elem in some_list:
#         if type(elem[1]) == int:
#             total_grade += elem[1]
#             if max_grade < elem[1]:
#                 max_grade = elem[1]
#             if min_grade > elem[1]:
#                 min_grade = elem[1]
#             if elem[1] > 90:
#                 students_over_some_grade.append(elem)
#
#     aver_grade = total_grade / len(some_list)
#     return max_grade, min_grade, aver_grade, students_over_some_grade
#
# resalt = find_info(students)
# print(resalt)

# У вас есть список products, в котором
# каждый элемент представляет собой кортеж с информацией о продукте:
# (название продукта, цена, количество).
# Напишите функцию analyze_products,
# которая анализирует этот список и возвращает следующую информацию:
#
# Средняя цена продукта.
# Самый дорогой продукт.
# Самый дешевый продукт.
# Список продуктов, у которых количество больше 10.

# products = [
#     ("apple", 1.5, 20),
#     ("banana", 0.5, 15),
#     ("orange", 2.0, 12),
#     ("grapes", 3.0, 8),
#     ("watermelon", 5.0, 5)
# ]
#
# def get_info(some_list: list):
#     total_sum = 0
#     max_price = float('-inf')
#     min_price = float('inf')
#     list_products = []
#     for elem in some_list:
#         name = elem[0]
#         price = elem[1]
#         counter = elem[2]
#         if max_price < price:
#             max_price = price
#         if min_price > price:
#             min_price = price
#         if counter > 10:
#             if elem not in list_products:
#                 list_products.append((name, counter))
#
#
#         total_sum += price
#         aver_price = total_sum / len(some_list)
#     return f'Самый дорогой продукт: {max_price}\n Самый дешевый продукт: {min_price}\n Средняя цена продукта {aver_price}\n Список продуктов, у которых количество больше 10: {list_products}'
#
#
# result = get_info(products)
# print(result)