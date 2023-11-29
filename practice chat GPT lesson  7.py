# Задача: Класс "Точка в пространстве"
# Создайте класс Point3D, представляющий точку в трехмерном пространстве.
# Каждая точка имеет координаты x, y, и z.
# Реализуйте метод __init__, который принимает значения x, y, и z
# и инициализирует соответствующие атрибуты.
# Реализуйте метод distance_to_origin, который вычисляет расстояние
# от точки до начала координат (0, 0, 0).
# Реализуйте метод move, который принимает значения dx, dy, dz и
# перемещает точку на указанное расстояние вдоль каждой из осей.
# import math
# class Point3D:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#         self.start_x = 0
#         self.start_y = 0
#         self.start_z = 0
#
#     def distance_to_origin(self):
#         return math.sqrt(((self.x - self.start_x))**2
#                          + ((self.y - self.start_y))**2
#                         + ((self.z - self.start_z))**2)
#
#     def move(self, dx, dy, dz):
#         self.x += dx
#         self.y += dy
#         self.z += dz
#
# p1 = Point3D(2, 5, 15)
# print(p1.distance_to_origin())
# print(p1.x)
# p1.move(4, 6, 18)
# print(p1.x)


