# ### Задача: Подсчет слов в тексте
# Напишите функцию, которая принимает текстовую строку и возвращает словарь,
# содержащий количество вхождений каждого слова в тексте.
# В этом случае, слова - это последовательности символов,
# разделенные пробелами, и мы игнорируем регистр букв.
# def word_count(text):
#     words = text.split()
#     dict_out = {}
#     for word in words:
#         if word not in dict_out:
#             dict_out[word] = 1
#         else:
#             dict_out[word] += 1
#     return dict_out

# Пример использования:
# text_example = "This is a simple example. This example is just for practice."
# result = word_count(text_example)
# print(result)
# Ожидаемый вывод:
# {'this': 2, 'is': 2, 'a': 1, 'simple': 1, 'example.': 2, 'example': 1, 'just': 1, 'for': 1, 'practice.': 1}
