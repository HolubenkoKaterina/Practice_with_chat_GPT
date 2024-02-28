import pandas as pd

# data = pd.read_csv('C:/Users/User/Downloads/archive (2)/jobs_in_data.csv', na_values='NA', decimal=',', skiprows=1)
# print(data.columns) #вывод всех названий колонок
# #print(data.head()) # вывод частично колонок и первые 5 значений в таблице
# area_index = data[data['Data DevOps Engineer'].str.contains('Principal')].index
# #print(area_index)
# data_area_index = ['Principal' if ind in area_index else 'No' for ind in data.index]
# data['Changes'] = data_area_index
# data = data.set_index(['Changes', 'Data DevOps Engineer']) # сортируете DataFrame по индексам.
# #print(data)
# areas = data.loc['Principal'] # выбираете только те строки, где значение 'Changes' равно 'Principal'.
# data = data.sort_index()
# print(areas)


# data_1 = pd.read_csv('C:/Users/User/Desktop/данные по вакансиям для сравнения/job_description.csv', na_values='NA', decimal=',', index_col='Category')
# data_2 = pd.read_csv('C:/Users/User/Desktop/данные по вакансиям для сравнения/job_data_merged_1.csv', na_values='NA', decimal=',', index_col='Category')
# data = pd.merge(data_1, data_2, left_index=True, right_index=True)
# если нет одинаковых указаных колонок с индексацией то в right_index= указываем колонку
# print(data_1.columns)
# print(data_2.columns)
#data.fillna(0, axis=1, inplace=True)
#print(data.mean())
# numeric_data = data.select_dtypes(include='number')
# print(numeric_data.mean())
# этот способ исключит ошибки попытки расчетов среднего значения в строковых значениях
#data = data.rename(columns={'VIN (1-10)': 'VIN'}) # переименование конкретной колонки
# print(data.columns)

# data_1 = pd.read_csv('C:/Users/User/Desktop/данные по вакансиям для сравнения/job_description.csv', na_values='NA', decimal=',')
# #print(data_1.columns)
# data_1 = data_1.rename(columns={'Unnamed: 0': 'порядковый номер', 'Category': 'категория', 'Description': "описание", 'Benefits': "преимущества",
#                                 'Requirement': "требования" })
# #print(data_1.loc[:, ('категория', 'требования', 'Requirements')])
# #print(data_1.iloc[319, :])
# data_1["Общие требования"] = data_1["требования"].combine_first(data_1["Requirements"])
# data_1.drop(columns=['Requirements', 'требования'], inplace=True)
#  # изменение исходного фрейма
# data_1.set_index('Общие требования', inplace=True)# индексацию по колонке
# print(data_1.head())


