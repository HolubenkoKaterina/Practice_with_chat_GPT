# У вас есть список студентов с их оценками за экзамены.
# Напишите программу, которая принимает этот список в качестве
# входных данных и вычисляет среднюю оценку для каждого студента,
# а затем выводит их имена и средние оценки.
# students = [
#     ("Анна", [85, 90, 92]),
#     ("Борис", [75, 80, 85]),
#     ("Виктория", [90, 95, 88])
# ]
# def ger_aver_grade_students(some_list: list):
#     new_list = []
#
#     for elem in some_list:
#
#         name = elem[0]
#         grade = elem[1]
#         total_grade = sum(grade)
#         aver_grade = total_grade / len(grade)
#         new_list.append((name, aver_grade))
#     return new_list
#
# result = ger_aver_grade_students(students)
# print(result)
# У вас есть список с информацией о товарах в интернет-магазине.
# Каждый элемент списка представляет собой кортеж, содержащий название товара,
# его цену и количество на складе.
# Напишите функцию, которая будет принимать этот список и возвращать следующую информацию:
#
# Среднюю цену товаров.
# Общую стоимость всех товаров на складе.
# Наименование товара с наибольшим количеством на складе.
products = [
    ("Ноутбук", 1000, 10),
    ("Смартфон", 600, 20),
    ("Планшет", 800, 15)
]
def get_info(some_list: list):
    total_sum = 0
    total_sum_product = 0
    aver = 0
    max_balance_goods = float('-inf')
    for elem in some_list:
        total_sum_product = elem[1] * elem[2]
        total_sum += total_sum_product
        aver = round(total_sum_product / len(some_list), 2)
        if max_balance_goods < elem[2]:
            max_balance_goods = elem[2]

    return f'остаток товара на сумму: {total_sum},\nмаксимальный остаток у товара: {max_balance_goods},\nсредняя цена товаров:  {aver}'
print(get_info((products)))
