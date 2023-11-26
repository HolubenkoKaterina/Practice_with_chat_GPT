# Задача: Класс для работы с файлами
# Создайте класс FileManager, который будет представлять
# простую систему управления файлами. У класса должны быть следующие методы:
# __init__(self, file_name): конструктор класса,
# который принимает имя файла и открывает его для записи.
# write_data(self, data): метод для записи данных в файл.
# Принимает данные в виде строки и записывает их в файл.
# read_data(self): метод для чтения данных из файла.
# Возвращает содержимое файла в виде строки.
# close_file(self): метод для закрытия файла.
# class FileManager:
#     def __init__(self, file_name):
#         self.file_name = file_name
#         self.file_handle = None
#
#     def write_data(self, data, path):
#         try:
#             with open(path, 'w', encoding='utf-8') as my_file:
#                 for string in data:
#                     my_file.write(string + '\n')
#                 self.file_handle = my_file  # Store the file handle
#         except ValueError as ex:
#             print(ex)
#
#     def read_data(self, path):
#         try:
#             with open(path, 'r', encoding='utf-8') as my_file:
#                 content = my_file.read()
#                 self.file_handle = my_file  # Store the file handle
#                 return content
#         except ValueError as ex:
#             print(ex)
#
#     def close_file(self):
#         if self.file_handle is not None:
#             self.file_handle.close()
#             print("File closed.")
#         else:
#             print("No file is currently open.")
#
# # Example usage:
# file_manager = FileManager("example.txt")
# data_to_write = ["Line 1", "Line 2", "Line 3"]
#
# file_manager.write_data(data_to_write, "example.txt")
#
# read_data = file_manager.read_data("example.txt")
# print(read_data)

file_manager.close_file()

