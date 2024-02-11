# Создайте дескриптор Password, который будет использоваться для хранения пароля.
# Пароль должен быть строкой, и его длина должна быть не менее 8 символов.
# Если устанавливаемый пароль не соответствует этим требованиям,
# генерируйте исключение ValueError с сообщением "Недопустимый пароль".
# Создайте класс User, в котором будут два атрибута: username и password.
# При установке значения атрибута password должна использоваться проверка
# через дескриптор Password.
# class Password:
#     def __get__(self, instance, owner):
#         return instance._password  # Возвращаем текущее значение пароля
#
#     def __set__(self, instance, value):
#         if len(value) < 8:
#             raise ValueError("Недопустимый пароль. Длина пароля должна быть не менее 8 символов.")
#         instance._password = value  # Устанавливаем значение пароля
#
# class User:
#     def __init__(self, username, password):
#         self.username = username
#         self._password = password  # Приватное поле для хранения пароля
#         self.password_validator = Password()  # Создаем экземпляр дескриптора Password
#
#     @property
#     def password(self):
#         return self.password_validator.__get__(self, User)  # Получаем значение пароля
#
#     @password.setter
#     def password(self, value):
#         self.password_validator.__set__(self, value)  # Устанавливаем значение пароля
#
# # Пример использования
# try:
#     user = User("Alice", "short")  # Попытка установить недопустимый пароль
# except ValueError as e:
#     print(e)
#
# # Попытка установить допустимый пароль
# user = User("Bob", "strongpassword")
# print(user.username, user.password)
