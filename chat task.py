# Напишите функцию word_frequency(text: str) -> dict,
# которая принимает на вход строку text и возвращает словарь,
# в котором ключами являются слова из строки, а значениями - количество раз,
# которое каждое слово встречается в тексте.
# При подсчете частоты слов необходимо игнорировать регистр символов и знаки препинания.

# def remove_substrings(text, substrings):
#     translation_table = str.maketrans("", "", substrings)
#     return text.translate(translation_table)
#
# text = "I want to go to the park to play with my dog."
# substrings = "to"
#
# result = remove_substrings(text, substrings)
# print(result)

# text = "Hello, world! This is a simple sentence, world."
# import string
# def text_conversion(text_to_convert: str):
#     punctuation = string.punctuation
#     text_out = text_to_convert.translate(str.maketrans('', '', punctuation))
#     # str.maketrans('', '', punctuation)
#     # метод что заменить, на что заменить, что удалить
#     return text_out.lower()
# print(text_conversion(text))
#
# def word_frequency(some_text: str):
#     text_to_work = text_conversion(some_text)
#     words = text_to_work.split()
#     dict_out = {}
#
#     for word in words:
#         if word not in dict_out:
#             dict_out[word] = 1
#
#         else:
#             dict_out[word] += 1
#     return dict_out
#
# print(word_frequency(text))

# Задача: Проверка на анаграмму

# Напишите функцию is_anagram, которая принимает две строки в качестве входных аргументов
# и возвращает True, если они являются анаграммами (то есть содержат одни и те же буквы в разном порядке),
# и False в противном случае. При проверке анаграммы не учитывают регистр букв и пробелы.
# word1 = "listen"
# word2 = "silent"
# def is_anagram(f_str: str, s_str: str):
#     f_str_new = f_str.lower().replace(' ', '')
#     s_str_new = s_str.lower().replace(' ', '')
#     if len(f_str_new) == len(s_str_new):
#         f = sorted(f_str_new, key=lambda let: let)
#         s = sorted(s_str_new, key=lambda let: let)
#         if f == s:
#             return True
#     return False
# print(is_anagram(word1, word2))

