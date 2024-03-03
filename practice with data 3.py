import numpy as np
import matplotlib.pyplot as plt

# file_path = 'C:/Users/User/Desktop/VideoGameUsage_Profile.csv'
# data = np.loadtxt(file_path, delimiter=',', skiprows=1, dtype=None)
#
# # Извлекаем числовые значения из первой строки
# numeric_values = [value for value in data[0] if value.isdigit()]
#
# # Преобразование значений в целые числа
# new_shape = tuple(map(int, numeric_values))
#
# # Удаление первой строки данных
# data = data[1:]
#
# # Преобразование строковых значений в числа в оставшихся данных
# data = data.astype(int)
#
# # Изменение формы данных
# reshaped_data = data.reshape(new_shape)
#
# plt.imshow(reshaped_data, cmap='Greys')
# plt.show()

# data = pandas.read_csv('C:/Users/User/Desktop/apple_quality.csv', na_values='NA', decimal=',')
# data.fillna(0, axis=1, inplace=True)
# # axis = 1 столбцы, axis = 0 строки, inplace=True будет изменен исходный обьект
# print(data.head())
# data_array = data.values # встроен.метод посмотреть значения
# print(data_array)
import pandas as pd

excel_file = pd.ExcelFile('C:/Users/User/Desktop/Sample - Superstore.xls')
# print(excel_file.sheet_names)# сначала надо увидеть названия листов в файле
# data = excel_file.parse(sheet_name=1) # распарсить данные на нужном листе (по индексу)
# print(data)
# print(data.head()) # увидеть заголовки
# print(excel_file.head())
#чтобы сразу прочитать все листы в файле и обьединить их в один фрейм
# Получаем названия всех листов в файле
sheet_names = excel_file.sheet_names
# print(sheet_names)
# Читаем все листы и объединяем их в один DataFrame
#all_data = pd.concat([excel_file.parse(sheet_name) for sheet_name in sheet_names]) # в короткой записи
#print(all_data)
# Создание списка временных DataFrame для каждого листа
dataframes = []
for sheet_name in sheet_names:
    dataframe = excel_file.parse(sheet_name)
    dataframes.append(dataframe)
all_data = pd.concat(dataframes, ignore_index=True)
#ignore_index=True используется для переиндексации результирующего DataFrame.
all_data['Order Date'] = pd.to_datetime(all_data['Order Date'], errors='coerce')
all_data['Ship Date'] = pd.to_datetime(all_data['Ship Date'], errors='coerce')
all_data['Quantity'] = pd.to_numeric(all_data['Ship Date'], errors='coerce')


#Эта строка кода конвертирует столбец 'Date' в формат datetime.
# pd.to_datetime - это функция pandas, которая преобразует объекты в формат datetime.
# Параметр errors='coerce' используется для замены любых некорректных значений
# в столбце на NaT (Not a Time), что полезно при обработке
# некорректных или отсутствующих данных в столбце дат.
# Выводим заголовки и первые строки объединенного DataFrame
#print(all_data.head())
#print(all_data['Order ID'])
print(all_data.head())
print(all_data.columns)
print(all_data[['Order Date', 'Ship Date', 'Quantity']].dtypes)
print(all_data.dtypes)
print(all_data['Quantity'])
rounded_mean = round(all_data['Quantity'].mean(), 2)
# можно увидеть число в привычной записи но в таком виде это строка, а не инт
# formatted_number = "{:.2f}".format(rounded_mean)
# print(formatted_number)
print(rounded_mean)



