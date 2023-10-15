from src.item import Item

"""Здесь надо написать тесты с использованием pytest для модуля item."""


# TestCase#1


def test_calculate_total_price():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000


def test_apply_discount():
    item1 = Item("Смартфон", 10000, 20)
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000.0


def test_instantiate_from_csv(tmp_path):
    csv_data = "name,price,quantity\nitem1,10.0,5\nitem2,20.0,3"
    file_path = tmp_path / "test_data.csv"
    with open(file_path, "w") as file:
        file.write(csv_data)
    items = Item.instantiate_from_csv(file_path)
    assert len(items) == 2
    assert len(Item.all) == 2


def test_string_to_number():
    assert Item.string_to_number("123") == 123
    assert Item.string_to_number("12.34") == 12
    assert Item.string_to_number("abc") == 0
    assert Item.string_to_number("") == 0

def test_repr():
    item = Item('Смартфон', 10000, 20)
    test_repr = "Item('Смартфон', 10000, 20)"
    assert repr(item) == test_repr

def test_str():
    item = Item('Холодильник', 10, 1)
    test_str = "Холодильник"
    assert str(item) == test_str
