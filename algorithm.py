# Задача: Поиск наибольшего произведения подмассива
#
# Дан массив целых чисел.
# Найдите наибольшее произведение непрерывного подмассива (последовательных элементов).
# numbers = [2, 3, -2, 4]
# def max_subarray_product(some_list: list):
#     max_prod = some_list[0]  # Инициализация максимального произведения первым элементом
#     curr_prod = some_list[0]  # Текущее произведение
#
#     for elem in some_list[1:]:
#         curr_prod *= elem
#         max_prod = max(max_prod, curr_prod)  # Обновление максимального произведения
#
#         # Сбрасываем текущее произведение, если оно становится нулевым или отрицательным
#         if curr_prod <= 0:
#             curr_prod = 1
#
#     return max_prod
#
# print(max_subarray_product(numbers))  # Ожидаемый вывод: 6

# Задача: Поиск пропущенного числа
#
# У вас есть список чисел от 1 до n включительно, за исключением одного числа.
# Напишите функцию, которая принимает этот список и возвращает пропущенное число.
# missing_number = ([1, 2, 4, 5, 6]) #=> 3
# missing_number2 = ([1, 2, 3, 4, 6]) #=> 5
# def find_missing_number(some_list: list):
#     total_sum = len(some_list) + 1
#     list_sum = (total_sum * (total_sum + 1))//2
#     actual_sum = sum(some_list)
#     result = list_sum - actual_sum
#     return result
# print(find_missing_number(missing_number2))
