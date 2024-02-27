import pandas as pd

data = pd.read_csv('C:/Users/User/Desktop/данные по вакансиям для сравнения/japan_birth.csv', na_values='Na', decimal=',')
#print(data.columns),
columns_to_keep = ['year', 'birth_total']# оставить только выбранные колонки
data = data[columns_to_keep]
data_not_null = data[data['birth_total'].notnull()]
#print(data_not_null)
data_zero = data[data['birth_total'] == 0]
#print(data_zero)
# Удалить строки с пропущенными значениями в столбце 'birth_total'
data = data.dropna(subset=['birth_total'])# удаление строк с пустыми значениями
#print((data['year']).dtype)
# Удалить строки с пропущенными значениями в 'birth_total'

data = data.dropna(subset=['birth_total'])
# # Преобразовать 'birth_total' в целые числа
data['birth_total'] = data['birth_total'].astype(int)
#
data.columns = data.columns.str.strip()
# data.set_index('year', inplace=True)  # Устанавливаем 'year' в качестве индекса
filtered_data = data[data['birth_total'] > 2200000]
print(filtered_data)
