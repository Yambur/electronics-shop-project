import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        all_price = (self.quantity * self.price)
        return all_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        raise TypeError("Складывать можно только объекты классов с родительским классом Item")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name[:10]

    @classmethod
    def instantiate_from_csv(cls, file_path: str):
        cls.all.clear()
        items = []
        with open(file_path, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for i in reader:
                name = i['name']
                price = float(i['price']) if 'price' in i else 0.0
                quantity = int(i['quantity']) if 'quantity' in i else 0
                item = cls(name, price, quantity)
                items.append(item)
        cls.all.extend(items)
        return items

    @staticmethod
    def string_to_number(string_num: str):
        try:
            if '.' in string_num:
                return int(float(string_num))
            else:
                return int(string_num)
        except ValueError:
            return 0

    def __repr__(self) -> str:
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.name}'
