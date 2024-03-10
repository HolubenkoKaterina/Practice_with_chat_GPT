# У вас есть список кортежей, каждый из которых содержит информацию
# о продажах товаров в разных магазинах.
# Каждый кортеж состоит из названия товара, цены за единицу товара и количества проданных единиц в каждом магазине.
# Напишите функцию calculate_total_profit, которая принимает этот список в качестве аргумента
# и возвращает общую прибыль от продажи всех товаров, учитывая различные цены в разных магазинах.
# В первом кортеже указаны цены за единицу товара в разных магазинах,
# а во втором - количество проданных единиц товара в каждом магазине.
# sales_data = [
#     [("Книга", 500), ("Фломастеры", 100), ("Бумага", 200)],
#     [(20, 50, 100), (10, 30, 50)]
# ]
# def calculate_total_profit(*args):
#     total_profit = 0
#     for product_prices, product_quantities in zip(*args):
#         for price, quantity in zip(product_prices, product_quantities):
#             try:
#                 total_profit += int(price) * int(quantity)
#             except ValueError:
#                 continue  # Пропускаем элементы, которые не являются числами
#     return total_profit
#
# print(calculate_total_profit(*sales_data))

# Задача: Поиск самого длинного слова в строке.
#
# Напишите функцию find_longest_word, которая принимает строку и возвращает самое длинное слово в этой строке.
# Если таких слов несколько и их длина одинакова, функция должна вернуть первое из них.
# text = "Python is a powerful programming language"
# def find_longest_word(some_text: str):
#     max_len = 0
#     find_word = ''
#     for word in some_text.split():
#         if len(word) > max_len:
#             max_len = len(word)
#             find_word = word
#     return f'длина слова {max_len},\nискомое слово {find_word}'
#
# print(find_longest_word(text))  # Ожидаемый результат: "programming"

# Задача: Проверка на анаграммы
# Напишите функцию are_anagrams, которая принимает две строки и возвращает True,
# если они являются анаграммами друг друга, и False в противном случае.
# Анаграммы - это слова, образованные перестановкой букв другого слова.
# Для упрощения считаем, что строки содержат только буквы алфавита без учета регистра и пробелов.
# word1 = "listen"
# word2 = "silent"
# def are_anagrams(text_1: str, text_2: str):
#     symbols1 = text_1.lower().replace(' ', '')
#     symbols2 = text_2.lower().replace(' ', '')
#     s1 = sorted(symbols1)
#     s2 = sorted(symbols2)
#     return s1 == s2
#
# print(are_anagrams(word1, word2))  # Ожидаемый результат: True
