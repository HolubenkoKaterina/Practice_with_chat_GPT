# ### Задача: Палиндромные подстроки
# Напишите функцию, которая принимает строку и возвращает количество палиндромных подстрок (не учитывая регистр и пробелы). Подстроки должны состоять как минимум из двух символов.

def count_palindromic_substrings(s):
    new_s = s.replace(' ', '')
    counter = 0
    if len(s) > 0:
        for ind in range(len(new_s) - 1):
            if new_s[ind] == new_s[ind + 1]:
                counter += 1
        return counter
    else:
        raise ValueError("вы не передаете текст! ")


# Пример использования:
input_str = "A man a plan a canal Panama"
result = count_palindromic_substrings(input_str)
print(result)
# Ожидаемый вывод:
# 7

