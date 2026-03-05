# 10. Отбор дат, находящихся в будущем.
# import datetime
# now_date = datetime.date.today()
# dates = ["2023-10-01", "2023-10-12", "2023-10-03", "2023-10-04", "2023-10-05"]
# # Преобразуем строки с датами в объекты datetime.date
# dates = [datetime.date.fromisoformat(date) for date in dates]
# # Отфильтруем даты, оставив только те, что находятся в будущем
# list_out = [date for date in dates if date > now_date]
# print(list_out)

# Sorted:
#
# 1. Сортировка списка чисел по возрастанию.
# import random
# list_numbers = random.sample(range(5, 45), random.randint(2, 14))
# print(list_numbers)
# list_out = sorted(list_numbers, key=lambda elem: elem)
# print(list_out)

# 2. Сортировка списка строк в алфавитном порядке.
# list1 = ["banana", "cherry", "date", "apple"]
# list_out = list(sorted(list1, key=lambda elem: elem))
# print(list_out)

# 3. Сортировка списка чисел по убыванию.
# list_out = list(sorted(list_numbers, key=lambda elem: elem, reverse=True))
# print(list_out)

# 4. Сортировка строк по длине.
# list1 = ["banana", "cherry", "date", "apple"]
# list_out = list(sorted(list1, key=lambda elem: len(elem)))
# print(list_out)

# 5. Сортировка списка кортежей по второму элементу.
# my_tuples = [(1, 'apple'), (2, 'banana'), (3, 'cherry'), (12, 'bananas')]
# list_out = list(sorted(my_tuples, key=lambda elem: elem[1]))
# print(list_out)

# 6. Сортировка списка словарей по значению определенного ключа.
# my_list = [
#     {'name': 'John Doe', 'age': 30, 'city': 'New York'},
#     {'name': 'Jane Smith', 'age': 25, 'city': 'Los Angeles'},
#     {'name': 'Bob Johnson', 'age': 35, 'city': 'Chicago'}
# ]
# list_out = list(sorted(my_list, key=lambda elem: elem['age']))
# print(list_out)

#