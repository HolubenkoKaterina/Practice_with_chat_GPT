# Создайте класс Student, представляющий студента. У студента должны быть следующие атрибуты:
# name (имя студента)
# age (возраст студента)
# grades (список оценок)
# Реализуйте следующие методы:
# Метод add_grade(grade), который добавляет оценку в список оценок студента.
# Метод get_average_grade(), который возвращает среднюю оценку студента.
# Метод is_excellent_student(), который возвращает True,
# если студент имеет среднюю оценку 4.5 или выше, и False в противном случае.
# Создайте несколько объектов студентов, добавьте им оценки и проверьте работу методов.
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average_grade(self):
        summa_grades = 0
        for grade in self.grades:
            summa_grades += grade
        aver = round(summa_grades / len(self.grades), 2)
        return aver

    def is_excellent_student(self):
        if self.get_average_grade() >= 4.5:
            return True
        else:
            return False


student1 = Student('Ivan Butenko', 21)
student1.add_grade(5)
student1.add_grade(3)
student1.add_grade(2)
student1.add_grade(4)
print(student1.is_excellent_student())
print(student1.get_average_grade())
student2 = Student('Ivanna Butenko', 22)
student2.add_grade(5)
student2.add_grade(5)
student2.add_grade(4)
student2.add_grade(2)
student2.add_grade(5)
print(student2.is_excellent_student())
print(student2.get_average_grade())