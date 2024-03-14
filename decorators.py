# Создайте декоратор, который принимает параметр "retry_count" и повторяет выполнение функции заданное количество
# раз в случае возникновения исключения.
'''# def decorator(retry_count):
#     def decorator_inner(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(retry_count +1):
#                 try:
#                     resalt = func(*args, **kwargs)
#                     return resalt
#                 except Exception as ex:
#                     if _ == retry_count:
#                         raise ex
#
#         return wrapper
#     return decorator_inner
# @decorator(retry_count=4)
# def summa(*args):
#     total_sum = 0
#     for arg in args:
#         if isinstance(arg, (list, tuple)):
#             for el in arg:
#                 if isinstance(el, int):
#                     total_sum += el
#                 if isinstance(el, str):
#                     if el.isdigit():
#                         total_sum += int(el)
#     return total_sum
#
#
# data2 = ('10', '10', 15)
# result = summa(data2)
# print(result)'''



# # Создайте декоратор, который делает первую букву результата выполнения функции заглавной.
'''# def decorator(func):
#     def wrapper(*args, **kwargs):
#         resalt = func(*args, **kwargs)
#         if isinstance(resalt, str):
#             return resalt.title()
#         else:
#             raise ValueError('не тот тип данных!')
#     return wrapper
# @decorator
# def change_text(some_text: str):
#     resalt = [word.lower() for word in some_text.split()]
#     return ' '.join(resalt)
# text = 'I LIKE PYTHON'
# resalt = change_text(text)
# print(resalt)'''

# Создайте декоратор, который записывает результат выполнения функции в файл.
'''# def derorator_log(file_name):
#     def decorator_inner(func):
#         def wrapper(*args, **kwargs):
#             resalt = func(*args, **kwargs)
#             with open(file_name, 'w', encoding='utf-8') as log_file:
#                 log_file.write(f"Результат выполнения функции {func.__name__}({args}, {kwargs}) = {resalt}\n")
#             return resalt
#         return wrapper
#     return decorator_inner
# @derorator_log(file_name='file_log.log')
# def plus(a, b):
#     return a + b
# resalt = plus(5, 10)
# print(resalt)'''

