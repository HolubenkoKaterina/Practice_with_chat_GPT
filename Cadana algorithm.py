# Задача: Поиск максимальной разницы

# Дан массив целых чисел. Необходимо написать функцию, которая
# найдет максимальную разницу между двумя элементами массива,
# где меньший элемент находится слева от большего элемента.
# nums = [7, 1, 5, 3, 6, 4]
# def max_profit(prices):
#     if len(prices) < 2:
#         return 0
#     max_profit = 0
#     min_price = prices[0]
#     for price in prices[1:]:
#         max_profit = max(max_profit, price - min_price)
#         min_price = min(min_price, price)
#     return max_profit
# print(max_profit(nums))  # Вывод: 5

# Задача: Поиск подмассива с максимальной суммой
#
# Напишите функцию max_subarray_sum, которая принимает список целых чисел
# и возвращает максимальную сумму подмассива (подряд идущих элементов) в этом списке.
# numbers = [-2, 1, 13, 4, -1, 2, 1, -5, 4]
#
# def max_subarray_sum(some_list: list):
#     max_sum = 0
#     current_sum = 0
#     for elem in some_list:
#         current_sum += elem
#         if current_sum < 0:
#             current_sum = 0
#         max_sum = max(max_sum, current_sum)
#     return max_sum
#
# print(max_subarray_sum(numbers))  # Вывод: 20



