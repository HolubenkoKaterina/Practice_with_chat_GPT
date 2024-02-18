# Задача: Система управления задачами (To-Do List)
# Разработайте простую систему управления задачами.
# В системе должны быть следующие классы:
# Задача (Task):
# Свойства: Заголовок, Описание, Статус (выполнена/не выполнена),
# Срок выполнения.
# Методы: Вывод информации о задаче.
# Список задач (TaskList):
# Свойства: Список задач.
# Методы: Добавление задачи, Удаление задачи,
# Вывод всех задач, Вывод невыполненных задач.
# Напишите пример использования этих классов,
# включая создание нескольких задач,
# их добавление в список, изменение статуса,
# вывод списка всех задач и списка невыполненных задач.
# Примечание: Вы можете добавить дополнительные методы
# или свойства в классы в соответствии с вашей логикой реализации.

class Task:
    def __init__(self, title, description, deadline):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.status = False

    def get_info(self):
        return f'Title: {self.title},\ndescription {self.description}\ndeadline: {self.deadline}'


class Tasklist:
    def __init__(self):
        self.task_list = []

    def add_task(self, task):
        self.task_list.append(task)


    def remove(self, task):
        if task in self.task_list:
            self.task_list.remove(task)
        else:
            raise ValueError('такой задачи в списке нет!')

    def get_task_list(self):
        return self.task_list

    def change_status(self, task):
        if task in self.task_list:
            task.status = not task.status
        else:
            raise ValueError('такой задачи в списке нет!')

    def get_uncompleted_tasks(self):
        uncompleted_tasks = []
        for task in self.task_list:
            if not task.status:
                uncompleted_tasks.append(self.task)



task1 = Task("Task 1", "Description for Task 1", "2023-12-31")
task2 = Task("Task 2", "Description for Task 2", "2023-12-15")

task_list = Tasklist()
task_list.add_task(task1)
task_list.add_task(task2)

print("All tasks:")
for task in task_list.get_task_list():
    print(task.get_info())


