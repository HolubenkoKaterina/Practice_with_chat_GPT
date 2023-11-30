# Давайте создадим класс Rectangle для представления прямоугольника.
# У прямоугольника есть длина (length) и ширина (width). Реализуйте следующие методы:
# __init__(self, length, width): конструктор, который инициализирует длину и ширину прямоугольника.
# area(self): метод, который возвращает площадь прямоугольника.
# perimeter(self): метод, который возвращает периметр прямоугольника.
# is_square(self): метод, который возвращает True,
# если прямоугольник является квадратом (длина равна ширине), и False в противном случае.
#
# class Rectangle:
#     def __init__(self, length, width):
#         self.width = width
#         self.length = length
#
#     def area(self):
#         return f'{self.width * self.length} площадь '
#
#     def perimeter(self):
#         return f'{(self.width * 2) + (self.length * 2)} периметр'
#
#     def is_square(self):
#         if self.length == self.width:
#             return True
#         else:
#             return False
#
# rectangle1 = Rectangle(15, 5)
# print(rectangle1.area())
# print(rectangle1.perimeter())
# print(rectangle1.is_square())