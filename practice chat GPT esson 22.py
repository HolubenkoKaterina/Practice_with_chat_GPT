# Разработайте программу для моделирования интернет-магазина электроники.
# В системе должны быть следующие классы:
# Товар (Product):
# Свойства: Название, Бренд, Цена, Наличие на складе, Гарантия (в месяцах).
# Методы: Вывод информации о товаре.
# Заказ (Order):
# Свойства: Список товаров, Общая сумма заказа, Статус заказа.
# Методы: Добавление товара в заказ, Расчет общей суммы, Изменение статуса заказа.
# Покупатель (Customer):
# Свойства: Имя, Фамилия, Адрес, Список совершенных заказов.
# Методы: Создание заказа, Добавление заказа в список совершенных заказов,
# Вывод информации о покупателе.
# Напишите пример использования этих классов, включая создание нескольких товаров,
# оформление заказов и вывод информации о покупателях и их заказах.

class Product:
    def __init__(self, name, brand, price, stock_availability, warranty):
        self.__name = name
        self.__brand = brand
        self.__price = price
        self.__stock_availability = stock_availability
        self.__warranty = warranty

    def __str__(self):
        return f'наименование {self.__name}\nбренд {self.__brand}\nцена {self.price_get}\nналичие на складе {self.get_stock_availability()}\nгарантия {self.__warranty}'

    @property
    def price_get(self):
        return self.__price

    def get_stock_availability(self):
        return self.__stock_availability

    def reduce_stock_availability(self):
        self.__stock_availability -= 1


class Order:
    def __init__(self):
        self.__List_goods = []
        self.__order_total = 0
        self.__order_status = False

    def add_product(self, product):
        self.__List_goods.append(product)
        self.__order_total += product.price_get

    @property
    def get_list_goods(self):
        return self.__List_goods


class Customer:
    def __init__(self, name, lastname, address):
        self.orders = []
        self.name = name
        self.lastname = lastname
        self.address = address

    def create_order(self, products):
        order = Order()
        for product in products:
            order.add_product(product)
        self.orders.append(order)

    def __str__(self):
        orders_info = "\n".join(f"Товар в заказе: {order.get_list_goods}" for order in self.orders)
        return f'Имя {self.name}\nФамилия {self.lastname}\nАдресс {self.address}\n Заказы: {orders_info}'


# Пример использования классов
product1 = Product("Телефон", "Samsung", 500, 10, 12)
product2 = Product("Ноутбук", "Dell", 1000, 5, 24)

customer = Customer("Иван", "Иванов", "ул. Пушкина, д. Колотушкина")

customer.create_order([product1, product2])

print(customer)
