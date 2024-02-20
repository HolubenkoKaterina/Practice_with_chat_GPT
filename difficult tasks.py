# Напишите функцию, которая принимает на вход число и возвращает функцию, проверяющую, является ли заданное число простым.
# def get_check_number(num: int):
#     def check_number_for_simple():
#         if num <= 1:
#             return False
#         if num <= 3:
#             return True
#         if num % 2 == 0 or num % 3 == 0:
#             return False
#         i = 5
#         while i * i <= num:
#             if num % i == 0 or num % (i + 2) == 0:
#                 return False
#             i += 6
#         return True
#     return check_number_for_simple
#
# number_to_check = int(input('Введите ваше число: '))
# resalt = get_check_number(number_to_check)
# print(resalt())

# Создайте функцию, которая генерирует случайный пароль заданной длины и набора символов.
# import random
# import string
#
# def get_parol(length: int):
#     def make_parol():
#         parol_element = string.digits + string.ascii_letters + string.punctuation
#         parol = ''.join(random.choice(parol_element) for _ in range(length))
#         return parol
#     return make_parol
#
# length_parol = int(input('Введите длину пароля: '))
# resalt = get_parol(length_parol)
# print(resalt())
# print(resalt())
# print(resalt())

# Реализуйте функцию-генератор последовательности Фибоначчи, используя замыкания.
# def get_fibonaci_list():
#     def fibonacci_func(num: int):
#         if num <= 1:
#             return []
#         if num == 1:
#             return [1]
#         if num == 2:
#             return [1, 2]
#
#         fibonacci_list = [1, 2]
#         for i in range(2, num):
#             next_fibonacci = fibonacci_list[i - 1] + fibonacci_list[i - 2]
#             fibonacci_list.append(next_fibonacci)
#
#         return fibonacci_list
#
#     return fibonacci_func
#
# number_for_fibonacci = int(input('Введите, сколько чисел Фибоначчи нужно вывести: '))
# resalt = get_fibonaci_list()
# print(resalt(number_for_fibonacci))
######################################################################3
# генератор чисел Фибоначчи
# def get_fibonacci_generator(number):
#     a, b = 0, 1
#     for _ in range(number):
#         yield b
#         a, b = b, a + b
#
# number = int(input('Введите количество чисел Фибоначчи: '))
# fibonacci_generator = get_fibonacci_generator(number)
#
# for num in fibonacci_generator:
#     print(num)
#################################################################################
# Реализуйте функцию, которая принимает число и возвращает функцию для проверки, является ли оно числом Фибоначчи.
# def wrapper():
#     fibonacci_list = [1, 2]
#
#     def check_fibonacci(number):
#         if number in fibonacci_list:
#             return True
#         while fibonacci_list[-1] < number:
#             next_fibonacci = fibonacci_list[-1] + fibonacci_list[-2]
#             fibonacci_list.append(next_fibonacci)
#             if next_fibonacci == number:
#                 return True
#         return False
#
#     return check_fibonacci
#
#
# number_to_check = int(input('Enter a number: '))
# resalt = wrapper()
# print(resalt(number_to_check))
###########################################################################################3
# numbers_add = [int(num) for num in input('Введите ваши числа через запятую: ').replace(',', '').split()]

#Напишите функцию для разбиения строки на подстроки заданной длины.
# text = 'i like PYTHON so much python my LOVE'
# def make_substr(some_text: str, lenght_substr: int):
#     some_sudstr = []
#     for elem in range(0, len(some_text), lenght_substr):
#         some_substring = some_text[elem:elem + lenght_substr]
#         some_sudstr.append(some_substring)
#
#     return some_sudstr
# resalt = make_substr(text,lenght_substr=3)
# print(resalt)


# 29. Вычислить сумму элементов в списке, находящихся между минимальным и максимальным элементами.
# my_list = [10, -35, 25, 7, -3, 42, -8, 8, -3]
# def summa_between_max_min_elem(some_list: list):
#     max_el = float('-inf')
#     min_el = float('inf')
#     sum_between = 0
#     for index, elem in enumerate(some_list):
#         if elem > max_el:
#             max_el = elem
#         if elem < min_el:
#             min_el = elem
#         min_index = some_list.index(min_el)
#         max_index = some_list.index(max_el)
#
#         # Определяем начальный и конечный индексы для суммирования
#         start_index = min(min_index, max_index) + 1
#         end_index = max(min_index, max_index)
#
#         # Суммируем элементы между минимальным и максимальным элементами
#         sum_between = sum(some_list[start_index:end_index])
#
#     return sum_between
#
# result = summa_between_max_min_elem(my_list)
# print(result)

# 20. Найти медиану списка.
# my_list = [10, -35, 25, 7, -3, 42, -8, 8, -3]
# def find_median(lst):
#     sorted_lst = sorted(lst)  # Сортируем список по возрастанию
#     n = len(sorted_lst)
#
#     if n % 2 == 1:  # Если список имеет нечетное количество элементов
#         median = sorted_lst[n // 2]  # Медиана - это средний элемент
#     else:  # Если список имеет четное количество элементов
#         middle1 = sorted_lst[(n - 1) // 2]  # Первый из двух средних элементов
#         middle2 = sorted_lst[n // 2]  # Второй из двух средних элементов
#         median = (middle1 + middle2) / 2.0  # Медиана - среднее значение двух средних элементов
#
#     return median
# resalt = find_median(my_list)
# print(resalt)

# 21. Найти моду списка (самый часто встречающийся элемент).
# my_list = [10, 25, 25, 7, -3, 42, -8, 8, -3, -3]
# def find_most_common_element(some_list: list):
#     element_count = {}  # Создаем словарь для подсчета количества вхождений каждого элемента
#
#     for el in some_list:
#         if el in element_count:
#             element_count[el] += 1
#         else:
#             element_count[el] = 1
#
#     most_common_element = None
#     max_count = 0
#
#     for el, count in element_count.items():
#         if count > max_count:
#             most_common_element = el
#             max_count = count
#
#     return most_common_element
# resalt = find_most_common_element(my_list)
# print(resalt)

# my_string = "Hello, world! Hello, Python!"
# substring = "Hello"
#
# last_index = my_string.rfind(substring)
#
# if last_index != -1:
#     print(f"Подстрока '{substring}' найдена на позиции {last_index}")
# else:
#     print(f"Подстрока '{substring}' не найдена в строке.")
#
# 38. Сложить элементы с одинаковыми индексами из всех вложенных списков.
# # list_to_sum = [[12, 4, 111], [111, 10, 10], [11, 12, 111], [11, 12, 110]]
# # first_len = len(list_to_sum[0])
# # list_out = [0] * first_len  # Инициализируем список нулями такой же длины, как первый вложенный список
# # flag = True
# # for sublist in list_to_sum:
# #     if len(sublist) != first_len:
# #         flag = False
# #         raise ValueError('Списки разной длины!')
# #
# #     for index, elem in enumerate(sublist):
# #         list_out[index] += elem
# #
# # if flag:
# #     print(list_out)

# 36. Извлечь первые N элементов из каждого вложенного списка и создать новый список.
# nested_list_6 = [[144, 16, 'ttttt'], [12321, 'lime', -100], [121, 144, 'kiwi']]
# list_out = []
# first_length = len(nested_list_6[0])  # Получим длину первого вложенного списка
# flag = True
# for sublist in nested_list_6:
#     if len(sublist) != first_length:
#         flag = False
#         break  # Если хоть один вложенный список имеет другую длину, завершаем цикл
#     list_out.append(sublist[2])
#
# if flag:
#     print(list_out)
# else:
#     print("Не все вложенные списки имеют одинаковую длину.")

# Удалить все символы пунктуации из каждой строки.
# import string
# text = ['I like python!', 'hellO my furry friend', '', 'Maman', '4458', '8', '!', 'ytikjvxtrud', '']
# text_out = []
# for elem in text:
#     clean = ''
#     for char in elem:
#         if char not in string.punctuation:
#             clean += char
#     text_out.append(clean)
# print(text_out)

import string
#
# text = ['i like python!', 'hello my furry friend', 'maman', '4458', '8', '!', '']
#
# vowels = {}
# consonants = {}
# punctuation = {}
# digits = {}
#
# vowes_chars = 'aouyie'
# punctuation_chars = string.punctuation
#
# for elem in text:
#     for char in elem.lower():
#         if char.isalpha():
#             if char in vowes_chars:
#                 if char in vowels:
#                     vowels[char] += 1
#                 else:
#                     vowels[char] = 1
#             else:
#                 if char in consonants:
#                     consonants[char] += 1
#                 else:
#                     consonants[char] = 1
#         elif char.isnumeric():
#             if char in digits:
#                 digits[char] += 1
#             else:
#                 digits[char] = 1
#         elif char in punctuation_chars:
#             if char in punctuation:
#                 punctuation[char] += 1
#             else:
#                 punctuation[char] = 1
#
# print("Гласные:", vowels)
# print("Согласные:", consonants)
# print("Цифры:", digits)
# print("Знаки пунктуации:", punctuation)

# Заменить все гласные буквы в строках на определенный символ.
# vowes_chars = 'aouyie'
# symbol_to_change = '*'
# text = ['i like python!', 'hello my furry friend', 'maman', '4458', '8', '!', '']
# list_out = []
# for elem in text:
#     word = ''
#     for char in elem.lower():
#         if char.lower() in vowes_chars:
#             word += symbol_to_change
#         else:
#             word += char
#     list_out.append(word)
# print(list_out)

# 25. Отсортируйте элементы словаря по значениям.
# my_dict = {'one': 1, 'two': 2, 'three': 3}
# # Сортируем элементы словаря по значениям и получаем список кортежей
# sorted_items = sorted(my_dict.items(), key=lambda x: x[1])
# # Создаем новый словарь на основе отсортированных элементов
# sorted_dict = {key: value for key, value in sorted_items}
# print(sorted_dict)

# Вычислить сумму цифр в каждом элементе списка чисел.
# import random
# list_numb = random.sample(range(15, 26), random.randint(1, 13))
# #последовательность чисел от 15 до 25, длина списка будет варьироватся от 1 до 12
# print(list_numb)
# list_out = []
#
# for num in list_numb:
#     summa = 0
#     for digit in str(num):
#         summa += int(digit)
#     list_out.append(summa)
#
# print(list_out)

# Удвоить каждую букву в каждом элементе списка строк.
# my_strings = ['apple', 'banana', 'cherry', 'date']
# list_out = []
# for words in my_strings:
#     new_words = ''
#     for letter in words:
#         if not letter.isdigit():
#             new_words += letter * 2
#     list_out.append(new_words)
# print(list_out)

# Преобразовать список имен в список инициалов (например, "John Smith" в "J. S.").
# names = ["John Smith", "Jane Doe", "Michael Johnson"]
# initials = []
# for name in names:
#     parts = name.split()
#     first_initial = parts[0][0].upper()
#     last_initial = parts[1][0].upper()
#     full_initials = f"{first_initial}. {last_initial}."
#     initials.append(full_initials)
# print(initials)
# Проверьте, все ли элементы списка являются простыми числами.
# import random
# def is_prime(num):
#    if num < 2:
#        return False
#    for i in range(2, int(num**0.5) + 1):
#        if num % i == 0:
#            return False
#    return True
# all_prime = all(is_prime(num) for num in my_list)
# if all_prime:
#     print("Все числа в списке являются простыми.")
# else:
#     print("Не все числа в списке являются простыми.")
# Проверьте, есть ли в списке хотя бы один элемент, являющийся степенью двойки.
# import math
# my_list = random.sample(range(-5, 55), random.randint(5, 10))
# print(my_list)
# resalt = any(math.log(elem, 2) for elem in my_list if isinstance(elem, int))
# print(resalt)
# Убедитесь, что в списке есть хотя бы один элемент, состоящий только из символов пунктуации.
# import string
# my_strings = ["ap4ple", "banana", "date", 4]
# resalt = any(all(char in string.punctuation for char in elem) for elem in my_strings if isinstance(elem, str))
# print(resalt)

# Используйте zip для соединения двух списков и создания нового списка строк.
# list1 = ["apple", "banana", "cherry", "date"]
# list2 = ["orange", "grape", "kiwi", "plum"]
# list3 = list(zip(list1, list2))
# list_out = [', '.join(elem) for elem in list3 ]
# print(list_out)

# 9. Сортировка списка строк по количеству гласных букв.
# my_list = ['apple', 'banana', 'cherry', 'bananas']
# vowes = 'aeouiy'
# list_out = []
#
# for elem in my_list:
#     counter = 0
#     for letter in elem:
#         if letter in vowes:
#             counter += 1
#     list_out.append((counter, elem))
# list_out.sort()  # Сортируем список по количеству гласных
# sorted_elements = [elem for _, elem in list_out]
# print(sorted_elements)

# енерация простіх чисел в заданном диапазоне
# def generate_primes(start, finish):
#     def is_prime(num):
#         if num < 2:
#             return False
#         for i in range(2, int(num ** 0.5) + 1):
#             if num % i == 0:
#                 return False
#         return True
#
#     return [num for num in range(start, finish+1) if is_prime(num)]
#
# primes = generate_primes(10, 30)
# print(primes)

# Создайте генератор, который производит все простые числа в двоичной системе счисления.
# def generate_primes(start, finish):
#     def is_prime(num):
#         if num < 2:
#             return False
#         for i in range(2, int(num ** 0.5) + 1):
#             if num % i == 0:
#                 return False
#         return True
#
#     for num in range(start, finish+1):
#         if is_prime(num):
#             yield num
#
# primes_generator = generate_primes(10, 30)
# for prime in primes_generator:
#     print(prime)
# 12. Создать файл, содержащий данные о сотрудниках в формате "имя фамилия, возраст, должность".
# Прочитать файл, вывести средний возраст сотрудников каждой должности.
# import pickle
# def write_file(path, data):
#     try:
#         with open(path, 'wb') as my_file:
#             pickle.dump(data, my_file)
#     except FileNotFoundError as er:
#         print(er)
#
# def read_aver_age(path):
#     try:
#         with open(path, 'rb') as my_file:
#             content = pickle.load(my_file)
#             avg_age_by_position = {}
#
#             for employee in content:
#                 _, age, position = employee.split(", ")
#                 age = int(age)
#
#                 if position in avg_age_by_position:
#                     avg_age_by_position[position][0] += age
#                     avg_age_by_position[position][1] += 1
#                 else:
#                     avg_age_by_position[position] = [age, 1]
#
#             for position, (total_age, num_employees) in avg_age_by_position.items():
#                 avg_age = total_age / num_employees
#                 print(f"Должность: {position}, Средний возраст: {avg_age}")
#
#     except FileNotFoundError as er:
#         print(er)
#
# employees_data = [
#     "Иван Иванов, 30, Менеджер",
#     "Петр Петров, 35, Разработчик",
#     "Мария Сидорова, 28, Аналитик",
#     "Ольга Николаева, 40, Менеджер",
#     "Алексей Кузнецов, 32, Разработчик",
#     "Екатерина Иванова, 27, Аналитик",
#     "Владимир Смирнов, 45, Директор",
# ]
# write_file('emp.bin', employees_data)
# read_aver_age('emp.bin')

# 21. Создать программу для хранения контактов. Реализовать добавление, редактирование и удаление контактов в файле.
# def write_file(path, data):
#     try:
#         with open(path, 'w', encoding='utf-8') as my_file:
#             for names in data:
#                 my_file.write(f"{names['имя']}, {names['номер']}\n")
#     except FileNotFoundError as er:
#         print(er)
#
# def add_contact(path, name_add, number_add):
#     new_contact = {"имя": name_add.title(), "номер": '+3' + number_add}
#     contacts.append(new_contact)
#     write_file(path, contacts)
#
# def read_contacts(path):
#     contacts = []
#     try:
#         with open(path, 'r', encoding='utf-8') as my_file:
#             for line in my_file:
#                 name, number = line.strip().split(', ')
#                 contacts.append({"имя": name, "номер": number})
#         return contacts
#     except FileNotFoundError as er:
#         print(er)
#
# def redactor_contacts(path, name_find):
#     contacts = read_contacts(path)
#     for contact in contacts:
#         if contact['имя'] == name_find:
#             print(f"Контакт найден: {contact['имя']} - {contact['номер']}")
#             what_change = input('1. Изменить имя? 2. Изменить номер? (1/2): ')
#             if what_change == '1':
#                 new_name = input('Введите новое имя: ')
#                 contact['имя'] = new_name
#                 print('Имя изменено')
#             elif what_change == '2':
#                 new_number = input('Введите новый номер: ')
#                 contact['номер'] = new_number
#                 print('Номер изменен')
#             else:
#                 print('Неправильный ввод. Введите 1 или 2.')
#             write_file(path, contacts)
#             return
#     print('Контакт не найден')
#
# def delete_contact(path, name_delete):
#     contacts = read_contacts(path)
#     for contact in contacts:
#         if contact['имя'] == name_delete:
#             contacts.remove(contact)
#             print(f"Контакт {contact['имя']} удален.")
#             write_file(path, contacts)
#             return
#     print('Контакт не найден')
#
# contacts = read_contacts('contacts.txt')
#
# # Примеры использования:
# add_contact('contacts.txt', name_add='катя', number_add="80967957008")
# redactor_contacts('contacts.txt', 'катя')
# delete_contact('contacts.txt', 'катя')

# Отсортируйте список в порядке убывания.
# list_out = []
# for num in numbers:
#     for ind in range(len(list_out)):
#         if num > list_out[ind]:
#             list_out.insert(ind, num)
#             break
#     else:
#         list_out.append(num)
# print(list_out)

# Поменяйте местами два элемента списка по их индексам.
# print(numbers)
# ind_change1 = 2
# ind_change2 = 4
# # Check if the indices are valid
# if ind_change1 < len(numbers) and ind_change2 < len(numbers):
#     # Swap the elements
#     numbers[ind_change1], numbers[ind_change2] = numbers[ind_change2], numbers[ind_change1]
# print(numbers)

# Удалите все вхождения определенного элемента из списка.
# print(numbers)
# elem_del = 30
# index = 0
# while index < len(numbers):
#     if numbers[index] == elem_del:
#         numbers.pop(index)
#     else:
#         index += 1
# print(numbers)

# Найдите разницу между соседними элементами списка.
# print(numbers)
# list_out = []
# for ind in range(len(numbers)-1):
#     list_out.append((numbers[ind+1] - numbers[ind-1]))
# print(list_out)

# Выведите элементы списка в обратном порядке, используя только срезы.
# print(numbers)
# list_out = []
# for ind in range(len(numbers)):
#     list_out.append(numbers[-(ind + 1)])
# print(list_out)


# Определите, является ли список палиндромом (читается одинаково слева направо и справа налево).
# is_palindrome = True
# for i in range(len(numbers)//2):
#     if numbers[i] != numbers[-(i+1)]:
#         is_palindrome = False
#         break
#
# if is_palindrome:
#     print("Список является палиндромом")
# else:
#     print("Список не является палиндромом")


#Создайте список, представляющий матрицу, и выполните операцию транспонирования.
# matrix = [
#     [1, 4, 7],
#     [2, 5, 8],
#     [3, 6, 9]
# ]
# matrix_out = []
# for rows in range(len(matrix[0])):
#     row = []
#     for strings in range(len(matrix)):
#         row.append(matrix[strings][rows])
#     matrix_out.append(row)
# print(matrix)
# print(matrix_out)

#генератор вложеного списка
# import random
# nested_list = [[random.randint(-11, 9) for _ in range(3)] for _ in range(3)]

# Рекурсивно найти среднее значение всех чисел во вложенных списках.
# def find_aver_in_nested_list(some_nested_list: list):
#     summa = 0
#     counter = 0
#     for elem in some_nested_list:
#         if isinstance(elem, list):
#             summa_nested, counter_nested = find_aver_in_nested_list(elem)
#             summa += summa_nested
#             counter += counter_nested
#         else:
#             summa += elem
#             counter += 1
#     aver = summa / counter if counter > 0 else 0
#     return summa, counter
#
# summa, counter = find_aver_in_nested_list(nested_list)
# aver = summa / counter if counter > 0 else 0
# print(aver)

# 21. Используй filter, чтобы выбрать из списка только числа, которые являются степенями двойки.
# import random
# import math
# nums = random.sample(range(1, 18), random.randint(5, 11))
# print(nums)
# def check(num):
#     return math.log2(num).is_integer()
#
# resalt = list(filter(check, nums))
# print(resalt)

# 22. Примени filter для выбора строк, в которых все символы уникальны.
# strings = ["hello", "world", "python", "unique", "characters"]
#
# def all_unique(spisok):
#     return all(spisok.count(char) == 1 for char in spisok)
#
# result = list(filter(all_unique, strings))
# print(result)
# p = all_unique(strings)
# print(p)

# 23. Используй filter, чтобы оставить только элементы списка, которые являются палиндромами.
# strings = ["hello", "world", "python", "unique", "characters", 'olo']
# def check_palindrom(elem):
#     return elem.lower() == elem.lower()[::-1]
# resalt = list(filter(check_palindrom, strings))
# print(resalt)

# 24. Примени filter для выбора чисел, которые являются произведением двух различных элементов списка.
# import random
#
# nums = random.sample(range(1, 100), 27)
# print(nums)
#
# def is_product_of_two(num):
#     return any(num == nums[i] * nums[j] for i in range(len(nums)) for j in range(len(nums)) if i != j)
#
# result = list(filter(is_product_of_two, nums))
# print(result)

# 25. Используй filter, чтобы оставить только строки с более чем одним гласным символом.
# my_list = ['abcde', 'aei', 'xyz', 'ouaie', 'hello', 'pqrst', 'aiou', 'aeiou', 'bcd', 'uoaie']
# print(my_list)
#
# vowels = 'aoeuiy'
# result = list(filter(lambda elem: sum(elem.count(v) for v in vowels) > 1, my_list))
# print(result)


# import random
#
# nums = random.sample(range(1, 100), 27)
# print(nums)
# def check_simple(number):
#     if number == 1:
#         return False
#     elif number == 2:
#         return True
#     elif number % 2 == 0:
#         return False
#     else:
#         # Проверяем делители от 3 до квадратного корня из числа
#         for i in range(3, int(number**0.5) + 1, 2):
#             if number % i == 0:
#                 return False
#         return True
# resalt = list(filter(check_simple, nums))
# print(resalt)

import random
#
# nums = random.sample(range(1, 100), 27)
# print(nums)
#
# def is_prime(index):
#     if index < 2:
#         return False
#     for i in range(2, int(index**0.5) + 1):
#         if index % i == 0:
#             return False
#     return True
#
# result = list(filter(lambda elem: is_prime(nums.index(elem)), nums))
# print(result)

# 27. Используй filter, чтобы оставить только строки, содержащие слово "python" в любом регистре.
# text = ['Hello, this is a Python example.',
#  'I love programming in Python.',
#  'This string does not contain the word Python.',
#  'Python and data science go hand in hand.',
#  'Let\'s explore the world of Python programming.',
#  'This is a random string without Python.',
#  'Python programming is widely used.',
#  'Learn Python to enhance your skills.',
#  'Coding in Python is fun!',
#  'Another string without Python.']
#
# result = list(filter(lambda elem: 'python' in elem.lower(), text))
# for line in result:
#     print(line)


# 28. Примени filter для выбора чисел, которые являются суммой двух предыдущих элементов списка.
# numbers = [1, 1, 3, 4, 7, 11, 28, 29, 47, 76]
# def check_sum_prev_num(numbers):
#     for ind in range(2, len(numbers)):
#         if numbers[ind] == numbers[ind - 1] + numbers[ind - 2]:
#             yield numbers[ind]
#
# result = list(check_sum_prev_num(numbers))
# print(result)

# 30. Примени filter для выбора элементов списка, которые являются кубами целых чисел.
# import math
# numbers = [1, 8, 27, 64, 5, 125, 216, 7, 343, 1000]
# print(numbers)
# resalt = list(filter(lambda elem: round(math.pow(elem, 1/3))**3 == elem, numbers))
# print(resalt)