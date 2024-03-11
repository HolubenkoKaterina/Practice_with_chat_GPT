# Напишите функцию find_unique_elements(some_list: list), которая принимает список
# some_list и возвращает новый список, содержащий только уникальные элементы исходного
# списка, сохраняя при этом порядок их первого появления.
# some_list = [1, 2, 3, 4, 2, 3, 5, 1, 6]
# def find_unique_elements(num_list: list):
#     list_out = []
#     for elem in num_list:
#         if elem not in list_out:
#             list_out.append(elem)
#         else:
#             pass
#     return list_out
# print(find_unique_elements(some_list))  # Вывод: [1, 2, 3, 4, 5, 6]
#
# Напишите функцию find_most_common_element(some_list: list),
# которая принимает список some_list и возвращает наиболее часто встречающийся
# элемент в списке. Если есть несколько элементов с одинаковой максимальной частотой,
# функция должна вернуть один из таких элементов, предпочтительно тот, который встречается раньше в списке.
# some_list = [1, 22, 3, 4, 22, 3, 5, 1, 6, 1, 22, 22]
# def find_most_common_element(slist: list):
#     dict_out = {}
#     for elem in slist:
#         if elem not in dict_out:
#             dict_out[elem] = 1
#         else:
#             dict_out[elem] += 1
#     maxim = max(dict_out, key=lambda elem: dict_out[elem])
#     return maxim
#
# print(find_most_common_element(some_list))  # Вывод: 22
#
# Представьте, что у вас есть список чисел, и вам нужно найти три числа,
# сумма которых равна заданной цели. Напишите функцию find_triplet(nums: List[int], target: int),
# которая принимает список чисел nums и целевое число target,
# и возвращает список из трех чисел, сумма которых равна цели.
# Если такие числа не существуют, функция должна вернуть пустой список.

# def three_sum(nums, target):
#     nums.sort()  # Сортируем входной список
#
#     for i in range(len(nums) - 2):
#         left = i + 1  # Указатель, начиная с элемента после текущего
#         right = len(nums) - 1  # Указатель на последний элемент
#
#         while left < right:
#             total = nums[i] + nums[left] + nums[right]
#
#             if total == target:
#                 return [nums[i], nums[left], nums[right]]  # Найдено тройственное суммирующееся до цели
#             elif total < target:
#                 left += 1  # Увеличиваем left для увеличения суммы
#             else:
#                 right -= 1  # Уменьшаем right для уменьшения суммы
#
#     return []  # В случае отсутствия тройки возвращаем пустой список
#
# # Пример использования
# nums = [1, 2, 3, 4, 5, 6, 7]
# target = 10
# print(three_sum(nums, target))  # Вывод: [1, 3, 6]
