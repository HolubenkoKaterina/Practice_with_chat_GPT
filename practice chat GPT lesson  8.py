# Реализуйте класс Car, представляющий автомобиль.
# У автомобиля должны быть атрибуты: make (марка), model (модель), year (год выпуска) и mileage (пробег).
# Класс должен иметь следующие методы:
# Метод display_info(), который выводит информацию об автомобиле, включая марку, модель, год выпуска и пробег.
# Метод drive(miles), который увеличивает пробег автомобиля на указанное количество миль.
# Метод change_owner(new_owner), который меняет владельца автомобиля на нового.
# class Car:
#     def __init__(self, make, model, year):
#         self.mileage = 0
#         self.make = make
#         self.model = model
#         self.year = year
#         self.owner = None
#     def display_info(self):
#         return f'марка {self.make} модель {self.model} год выпуска {self.year} пробег {self.mileage}'
#
#     def drive(self, mileage ):
#         self.mileage += mileage
#
#     def change_owner(self, new_owner):
#         self.owner = new_owner
#         return self.owner
#
#     def get_owner(self):
#         return self.owner
#
# car1 = Car('bmw', '7', '2005')
# print(car1.display_info())
# car1.drive(500)
# car1.change_owner('petrov')
# print(car1.display_info())
# print(car1.get_owner())

