import csv


class InstantiateCSVError(Exception):
    pass


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name, price, quantity) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        cost_product = self.price * self.quantity
        return cost_product

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate
        """
        Проверяет, что длина наименования товара не больше 10 симвовов. 
        В противном случае, 
        обрезать строку (оставить первые 10 символов)
        """

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) <= 10:
            self.__name = value
            print(f'Корректное название - {value}')
        else:
            self.__name = value[:10]
            print(f'Длинное слово - {value[:10]}')

    @classmethod
    def instantiate_from_csv(cls, filepath='../src/items.csv'):
        try:
            cls.all = []
            with open(filepath, newline='', encoding='cp1251') as csvfile:
                reader = csv.DictReader(csvfile)
                for i in reader:
                    if 'name' not in i or 'price' not in i or 'quantity' not in i:
                        raise InstantiateCSVError(f'Файл {filepath} поврежден')
                    a = cls(i['name'], i['price'], i['quantity'])

        except FileNotFoundError:
            raise FileNotFoundError(f"Отсутствует файл {filepath}")

    @staticmethod
    def string_to_number(name):
        return int(float(name))

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self) -> str:
        return f'{self.name}'

    def __add__(self, other):
        """
        Метод сложения количества товаров двух классов
         """

        if not isinstance(other, Item):
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
        else:
            return self.quantity + other.quantity
