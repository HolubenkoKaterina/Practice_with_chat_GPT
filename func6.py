# Проверить, есть ли хотя бы одна строка в списке, начинающаяся с заглавной буквы, используя any.
# text = ['My Mind', 'Coffe Is Fu', 'Mama Help Me!']
# check = any(elem.istitle() for elem in text)
# print(check)

# Проверить, есть ли хотя бы один элемент в списке, находящийся в диапазоне от 5 до 15, используя any.
# list1 = [16, 20, 19]
# check = any(elem in range(5, 16) for elem in list1)
# print(check)

# Проверить, все ли элементы с одинаковыми индексами из двух списков равны между собой.
# list1 = [10, 15, 20, 25]
# list2 = [10, 15, 20, 25]
# check = all(elem == element for elem, element in zip(list1, list2))
# print(check)

# Создать список, состоящий из строк, где каждая строка содержит
# элементы с одинаковыми индексами из разных списков, объединенных через zip.
# list1 = ['we can', 'she can', 'he can']
# list2 = [10, 15, 20, 25]
# resalt_union = list(zip(list1, list2))
# print(resalt_union)

# Найти максимальное значение среди сумм пар элементов с одинаковыми индексами из двух списков, объединенных через zip.
# list1 = [5, 15, 20, 25]
# list2 = [10, 15, 20, 25]

# Проверить, все ли числа в списке принадлежат к простым числам, используя all.
# list1 = [7, 2]
# def is_prime(number: int):
#     if number <= 1:
#         return False
#     for i in range(2, int(number ** 0.5) + 1):
#         if number % i == 0:
#             return False
#     return True
# check = all(is_prime(elem) for elem in list1)
# print(check) #жесть просто с этими простыми числами

# Проверить, все ли элементы вложенных списков положительны, используя all.
# list_some = [
#     [1, 2, 3],
#     [4, 5, -6],
#     [7, 8, 9]]
# check = all(all(elem > 0 for elem in element) for element in list_some)
# print(check)

# Проверить, все ли элементы в списке являются степенями двойки, используя all.
# def is_power_of_two(number: int):
#     return number > 0 and (number & (number - 1)) == 0
# list1 = [8, 2, 16]
# check = all(is_power_of_two(elem) for elem in list1)
# print(check)

# Проверить, есть ли хотя бы один элемент в списке, являющийся степенью двойки, используя any.
# def check_stepen_2(elem: int):
#     return elem > 0 and (elem & (elem - 1)) == 0
# list1 = [8, 2, 16, 22]
# check = any(check_stepen_2(elem) for elem in list1)
# print(check)

# Проверить, есть ли хотя бы одна строка в списке, содержащая хотя бы одну цифру, используя any.
# list1 = ['16', '14', 'abc', 'abc111']
# check = any(any(element.isdigit() for element in elem) for elem in list1) # ну тут не очень
# print(check)