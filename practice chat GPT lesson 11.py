# давайте создадим класс для представления магазина, управляющего продуктами. Реализуйте следующие шаги:
# Создайте класс Product с методом __init__, который принимает название продукта
# (name), цену (price) и количество (quantity). Инициализируйте соответствующие атрибуты объекта.
# Добавьте метод display_info, который выводит информацию о продукте в формате:
# "Продукт: [name], Цена: [price], Количество: [quantity]".
# Реализуйте метод increase_quantity, который принимает значение
# amount и увеличивает количество продукта на указанное количество.
# Реализуйте метод sell_product, который принимает значение amount
# и уменьшает количество продукта на указанное количество.
# При этом проверьте, чтобы количество продукта не стало отрицательным.

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
       print( f'Продукт: {self.name}, Цена: {self.price} , Количество: {self.quantity}')

    def increase_quantity(self, amount):
        self.quantity += amount
        return self.quantity

    def sell_product(self, amount):
        if self.quantity >= amount:
            self.quantity -= amount
            return self.quantity
        else:
            raise ValueError('Недостаточно продуктов для продажи.')

tv1 = Product('sumsung GT-8', 10500)
tv1.increase_quantity(5)
tv1.sell_product(1)
print(tv1.display_info())
tv2 = Product('sumsung GT-8', 10000)
tv2.increase_quantity(10)
tv2.sell_product(2)
print(tv2.display_info())
tv3 = Product('sumsung GT-8', 8500)
tv3.increase_quantity(15)
tv3.sell_product(11)
print(tv3.display_info())
tv4 = Product('sumsung GT-8', 7000)
tv4.increase_quantity(6)
tv4.sell_product(7)
print(tv4.display_info())







