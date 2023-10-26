from src.item import Item
import pytest

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


@pytest.mark.parametrize("item1_quantity, item2_quantity, expected_result", [
    (1, 2, 3),
    (0, 5, 5),
    (3, 3, 6),
    (10, 20, 30)
])
def test_add_item(item1_quantity, item2_quantity, expected_result):
    item1 = Item("item1", 10.0, item1_quantity)
    item2 = Item("item2", 20.0, item2_quantity)
    result = item1 + item2
    assert result == expected_result

    with pytest.raises(TypeError):
        # Попробуйте сложить Item с чем-то другим
        item1 + "some_string"
