# Задача: Работники в компании
# Создайте два класса: Employee и Company.
# Employee должен иметь следующие атрибуты:
# name (строка) - имя сотрудника.
# position (строка) - должность сотрудника.
# salary (число) - зарплата сотрудника.
# Также у класса Employee должен быть метод display_info(),
# который выводит информацию о сотруднике в виде строки.
# Company должен иметь следующие атрибуты:
# name (строка) - название компании.
# employees (список объектов Employee) - список сотрудников компании.
# Также у класса Company должен быть метод add_employee(employee),
# который добавляет сотрудника в список компании,
# и метод list_employees(), который выводит информацию о всех сотрудниках компании.
#
# class Employee:
#     def __init__(self, name, position, salary):
#         self.name = name
#         self.position = position
#         self.salary = salary
#
#     def display_info(self):
#         return f'{self.name}({self.position})$ {self.salary}'
#
#
#
#
#
# class Company:
#
#     def __init__(self, name):
#         self.name = name
#         self.employees = []  # Используем атрибут для хранения сотрудников
#
#     def list_employees(self, company):
#         for emloyee in self.employees:
#             print(emloyee.display_info())
#
#     def add_employee(self, employee):
#         if employee not in self.employees:
#             self.employees.append(employee)
#         else:
#             raise ValueError('акой сотрудник уже в базе есть! ')
#
# # Пример использования
# employee1 = Employee("John Doe", "Developer", 50000)
# employee2 = Employee("Jane Smith", "Designer", 60000)
#
# company = Company("Tech Solutions")
#
# company.add_employee(employee1)
# company.add_employee(employee2)
#
# company.list_employees('Tech Solutions')

# Напишите класс Stack, представляющий собой стек.
# Стек - это структура данных, которая работает по принципу
# "последний вошел, первый вышел" (Last In, First Out - LIFO).
# У стека есть следующие методы:
# push(item): Добавляет элемент в верхнюю часть стека.
# pop(): Удаляет и возвращает элемент из верхней части стека. Если стек пуст, вернуть None.
# peek(): Возвращает элемент из верхней части стека, не удаляя его. Если стек пуст, вернуть None.
# is_empty(): Возвращает True, если стек пуст, и False в противном случае.

# class Stack:
#     stack_list = []
#     def push(self, item):
#         Stack.stack_list.append(item)
#
#     def pop(self):
#         Stack.stack_list.pop()
#         return Stack.stack_list
#
#     def peek(self):
#         if not Stack.stack_list:
#             return None
#         else:
#             return Stack.stack_list[-1]
#
#     def is_empty(self):
#         if not Stack.stack_list :
#             return True
#         else:
#             return False
#
#     def getter_stack(self):
#         return Stack.stack_list
#
# el1 = Stack()
# el1.push(1)
# el1.push(2)
# el1.push(3)
# el1.push(4)
# el1.push(5)
# print(el1.getter_stack())
# print(el1.peek())
# print(el1.is_empty())
# print(el1.peek())
# el1.pop()
# print(el1.peek())
# print(el1.getter_stack())



