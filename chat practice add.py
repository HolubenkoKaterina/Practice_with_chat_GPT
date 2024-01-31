### Задача: Управление животными в зоопарке
# 1. Создайте класс `Zoo`, который будет представлять зоопарк.
# У зоопарка должны быть атрибуты:
#    - `animal_list`: список для хранения животных в зоопарке.
# 2. Создайте класс `Animal`, представляющий животное в зоопарке.
# У животного должны быть атрибуты:
#    - `name`: имя животного.
#    - `species`: вид животного.
# 3. Реализуйте методы для класса `Zoo`:
#    - `add_animal(animal)`: добавляет животное в зоопарк.
#    - `remove_animal(animal)`: удаляет животное из зоопарка.
#    - `get_animal_count()`: возвращает текущее количество животных в зоопарке.
# 4. Переопределите метод `__str__` в обоих классах для красивого вывода информации.
# zoo = Zoo()
# lion = Animal("Leo", "Lion")
# tiger = Animal("Tom", "Tiger")
# elephant = Animal("Ellie", "Elephant")
# zoo.add_animal(lion)
# zoo.add_animal(tiger)
# zoo.add_animal(elephant)
# print(zoo)  # Вывод информации о зоопарке
# print(f"Number of animals in the zoo: {zoo.get_animal_count()}")
# zoo.remove_animal(tiger)
# print(zoo)  # Вывод информации о зоопарке после удаления
# print(f"Number of animals in the zoo: {zoo.get_animal_count()}")

class Zoo:
    def __init__(self, animal_list: list = None):
        self.animal_list = animal_list or []

    def __str__(self):
        return '\n'.join(str(animal) for animal in self.animal_list)

    def __add__(self, other):
        if isinstance(other, Animal):
            self.add_animal(other)
            return self
        else:
            raise ValueError("Can't add non-Animal object to Zoo")

    def __iadd__(self, other):
        if isinstance(other, Animal):
            self.add_animal(other)
            return self
        else:
            raise ValueError("Can't add non-Animal object to Zoo")

    def add_animal(self, animal):
        self.animal_list.append(animal)

    def remove_animal(self, animal_find):
        for animal in self.animal_list:
            if animal == animal_find:
                self.animal_list.remove(animal)
                return
        raise ValueError('Такого животного в зоопарке нет!')

    def get_animal_count(self):
        return len(self.animal_list)


class Animal:
    def __init__(self, name: str, species: str):
        self.species = species
        self.name = name

    def __str__(self):
        return f'Имя животного {self.name}, его вид {self.species}'

# Пример использования
zoo = Zoo()
lion = Animal("Leo", "Lion")
tiger = Animal("Tom", "Tiger")
elephant = Animal("Ellie", "Elephant")

zoo += lion  # Использование __iadd__
zoo += tiger
zoo += elephant

print(zoo)
print(f"Number of animals in the zoo: {zoo.get_animal_count()}")

# Создание нового зоопарка путем сложения (использование __add__)
new_zoo = zoo + Animal("Alex", "Alligator")
print(new_zoo)
print(f"Number of animals in the new zoo: {new_zoo.get_animal_count()}")
