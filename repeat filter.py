# 21. Используй filter, чтобы выбрать из списка только числа, которые являются степенями двойки.
import random
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

# # 24. Примени filter для выбора чисел, которые являются произведением двух различных элементов списка.
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

# 26. Примени filter для выбора элементов списка, чьи индексы являются простыми числами.
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

# import random
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

# 29. Используй filter, чтобы оставить только строки, в которых все слова начинаются с одной и той же буквы.
# text_list = [
#     "Sunrise starts silently.",
#     "Elephants eat enormous apples.",
#     "Jumping jellyfish just jolt.",
#     "Apples are awesome and bananas better.",
#     "Giraffes gracefully graze green grass."
# ]
# def check_start(text):
#     for string in text.split():
#         return string.lower().startswith('j')
#
# resalt = list(filter(check_start, text_list))
# print(resalt)

# 30. Примени filter для выбора элементов списка, которые являются кубами целых чисел.
# import math
# numbers = [1, 8, 27, 64, 5, 125, 216, 7, 343, 1000]
# print(numbers)
# resalt = list(filter(lambda elem: round(math.pow(elem, 1/3))**3 == elem, numbers))
# print(resalt)