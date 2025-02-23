Создайте словарь, в котором значения являются списками.
Обновите значение в списке, который является значением в словаре.
# my_dict = {
#     'ключ1': [1, 2, 3],
#     'ключ2': ['a', 'b', 'c'],
#     'ключ3': [True, False, True]
# }
# for key, val in my_dict.items():
#     my_dict['ключ2'][1] = 40
# print(my_dict)

Найдите ключ, соответствующий максимальному значению в словаре.
Найдите ключ, соответствующий минимальному значению в словаре.
# my_dict = {
#     'ключ1': [1, 2, 3],
#     'ключ2': [4, 5, 6],
#     'ключ3': [7, 8, 9]
# }
# min_val = float('inf')
# max_val = float('-inf')
#
# for key, val in my_dict.items():
#     for elem in val:
#         if isinstance(elem, int):  # Проверяем, является ли элемент целым числом
#             if elem > max_val:
#                 max_val = elem
#             if elem < min_val:
#                 min_val = elem
#
# print(min_val, max_val)

# 22. Найдите ключ, соответствующий минимальному значению в словаре.
# my_dict = {
#     18: [1, 2, 3],
#     28: [4, 5, 6],
#     'ключ3': [7, 8, 9]
# }
# min_key = float('inf')
# for key, val in my_dict.items():
#     if isinstance(key, int):
#         if key < min_key:
#             min_key = key
# print(min_key)

# 23. Удалите все элементы с определенным значением.
# my_dict = {
#     'one': 1,
#     'two': 2,
#     'three': 3,
#     'four': 4,
#     'five': 5
# }
# def del_some_value(some_dict: dict, value_delete):
#     for key, val in some_dict.items():
#         if val == value_delete:
#             del [val]
#     return some_dict
# print(del_some_value(my_dict, value_delete=3))
# print(del_some_value(my_dict, value_delete=15))

