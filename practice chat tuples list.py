# есть список кортежей,
# представляющих информацию о студентах в разных классах.
# Каждый кортеж содержит имя студента, его возраст,
# класс и список оценок по различным предметам.
# Напишите функцию calculate_class_average_grades,
# которая принимает этот список в качестве аргумента и
# возвращает словарь, в котором ключами являются номера классов,
# а значениями - средний балл всех студентов в каждом классе.
# students_data = [
#     ("Иванов", 15, 10, [4, 5, 3, 4, 5]),
#     ("Петров", 16, 11, [3, 4, 4, 4, 5]),
#     ("Сидоров", 17, 10, [5, 5, 5, 5, 5]),
#     ("Козлов", 15, 11, [4, 5, 4, 4, 5])
# ]
#
# def calculate_class_average_grades(some_data: list):
#     students_aver_grades_on_class = {}
#     students_count_by_class = {}
#     for elem in some_data:
#         grades_stud = elem[3]
#         clas = elem[2]
#         summa_grades = sum(grades_stud)
#
#         if clas not in students_count_by_class:
#             students_count_by_class[clas] = len(grades_stud)
#         else:
#             students_aver_grades_on_class[clas] += len(grades_stud)
#
#         if clas not in students_aver_grades_on_class:
#             students_aver_grades_on_class[clas] = summa_grades
#         else:
#             students_aver_grades_on_class[clas] += summa_grades
#     for clas, summa_grades in students_aver_grades_on_class.items():
#         students_aver_grades_on_class[clas] /= students_count_by_class[clas]  # Делим сумму на количество студентов
#     return students_aver_grades_on_class
#
# print(calculate_class_average_grades(students_data))


# У вас есть список кортежей, каждый из которых содержит информацию о разных студентах.
# Каждый кортеж состоит из имени студента, его возраста и оценки за тест.
# Напишите функцию calculate_average_grade, которая принимает этот список в качестве аргумента
# и возвращает среднюю оценку всех студентов.
# students_data = [
#     ("Алексей", 20, 85),
#     ("Елена", 21, 90),
#     ("Иван", 19, 75),
#     ("Мария", 22, 88)
# ]
# def calculate_average_grade(data: list):
#     suma = 0
#     for elem in data:
#         grade = elem[2]
#         suma += grade
#         aver = suma / len(data)
#     return aver
# print(calculate_average_grade(students_data))  # Ожидаемый результат: 84.5


# У вас есть список кортежей, каждый из которых содержит информацию о продажах разных
# товаров в разных магазинах. Каждый кортеж состоит из названия товара,
# цены за единицу товара и количества проданных единиц в каждом магазине.
#
# Напишите функцию calculate_total_profit, которая принимает
# этот список в качестве аргумента и возвращает общую прибыль от
# продажи всех товаров, учитывая различные цены в разных магазинах.
# sales_data = [
#     [("Книга", 500), ("Фломастеры", 100), ("Бумага", 200)],
#     [(20, 50, 100), (10, 30, 50)]
# ]
# def calculate_total_profit(data: list):
#     total_profit = 0
#
#     # Перебираем данные о товарах и продажах
#     for products_prices, products_quantities in zip(data[0], data[1]):
#         product_profit = 0
#
#         # Извлекаем цену за единицу товара и количество проданных единиц
#         price = products_prices[1]  # Цена за единицу товара
#         for quantity in products_quantities:  # Количество проданных единиц
#             product_profit += price * quantity
#
#         # Добавляем прибыль от продажи данного товара к общей прибыли
#         total_profit += product_profit
#
#     return total_profit
#
#
# print(calculate_total_profit(sales_data))
# 

