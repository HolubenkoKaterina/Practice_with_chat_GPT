# Напишите функцию calculate_sum, которая принимает список чисел в качестве аргумента
# и возвращает сумму всех чисел в этом списке, умноженную на их индекс (позицию в списке),
# если число четное. Если число нечетное, оно не учитывается при подсчете.

# def calculate_sum(nums_list: list):
#     summa = 0
#     for elem, ind in enumerate(nums_list):
#         if elem % 2 != 0 and ind % 2 == 0:
#             summa += elem * ind
#     return summa
#
# numbers = [1, 2, 3, 4, 5]
# print(calculate_sum(numbers))

#
# Напишите функцию has_duplicates, которая принимает список и возвращает True,
# если в списке есть хотя бы один дубликат, и False в противном случае.

# def has_duplicates(some_list: list):
#     unique_elements = set()
#     for elem in some_list:
#         if elem in unique_elements:
#             return True
#         unique_elements.add(elem)
#     return False
#
# numbers = [1, 2, 3, 4, 5]
# words = ["apple", "banana", "apple", "orange"]
#
# print(has_duplicates(numbers))  # Вывод: False
# print(has_duplicates(words))    # Вывод: True


