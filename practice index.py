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
#
# Напишите функцию count_unique_words, которая принимает строку и возвращает количество уникальных слов в этой строке.
# Слова считаются уникальными независимо от регистра символов (то есть "Hello" и "hello" считаются одним и тем же словом).

# text = "Python is a powerful programming language. Python is also easy to learn."
# def count_unique_words(some_text: str):
#     some_text_new = some_text.lower().split()
#     words_out = set(some_text_new)
#     counter = len(words_out)
#     return f'{counter} кол-во уникальных слов в нашем тексе'
# print(count_unique_words(text))

# У вас есть список студентов и их оценки за несколько предметов. Напишите функцию Python,
# которая принимает этот список в качестве входных данных и возвращает словарь,
# в котором ключами являются имена студентов, а значениями - средние оценки каждого студента.
# students_grades = {
#     "Анна": [85, 90, 92],
#     "Борис": [75, 80, 85],
#     "Виктория": [90, 95, 88]
# }
#
#
# def calculate_average_grade(some_dict: dict):
#     students = {}
#     for name, grades in some_dict.items():
#         counter = 0
#         if name not in students:
#             for grade in grades:
#                 counter += grade
#             aver = counter / len(grades)
#             students[name] = aver
#     return students
#
#
# print(calculate_average_grade(students_grades))
