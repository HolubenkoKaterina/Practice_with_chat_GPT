# давайте рассмотрим задачу о создании класса Triangle для представления треугольника.
# Реализуйте следующие методы:
# __init__(self, side1, side2, side3): конструктор, который инициализирует стороны треугольника.
# get_perimeter(self): метод для вычисления и возврата периметра треугольника.
# get_area(self): метод для вычисления и возврата площади треугольника. Используйте формулу Герона:
# area= # s⋅(s−a)⋅(s−b)⋅(s−c)
#где  s - полупериметр треугольника, # a,b,c - длины сторон треугольника.
import math
class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def get_perimeter(self):
        return  self.side1 + self.side2 + self.side3

    def half_perimetr(self):
        return self.get_perimeter() / 2

    def get_area(self):
        return (self.half_perimetr() *
                (self.half_perimetr() - self.side1) *
                (self.half_perimetr() - self.side2) *
                (self.half_perimetr() - self.side3)) ** 0.5



tr1 = Triangle(5, 4, 6)
print(tr1.get_perimeter())
print(tr1.half_perimetr())
print(tr1.get_area())