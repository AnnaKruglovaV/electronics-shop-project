from src.item import Item
import pytest

from src.phone import Phone


@pytest.fixture
def position():
    return Item("Смартфон", 100, 1)


@pytest.fixture
def phone1():
    return Phone("IPhone", 30000, 10, 2)


def test_item_init(position):
    assert position.name == "Смартфон"
    assert position.price == 100
    assert position.quantity == 1


def test_calculate_total_price():
    item = Item('Смартфон', 20000, 100)
    assert item.calculate_total_price() == 2000000


def test_apply_discount():
    item = Item('Смартфон', 2000, 3)
    Item.pay_rate = 0.1

    item.apply_discount()

    assert item.price == 200.0


def test_name_setter():
    item = Item('Телефон', 10000, 5)
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'


def test_name_setter_truncate():
    item = Item('Телефон', 25000, 3)
    item.name = 'Суперсмартфон'
    assert item.name == 'Суперсмарт'


def test_instantiate_from_csv():
    Item.instantiate_from_csv('src/items.csv')
    assert len(Item.all) == 5

    item1 = Item.all[0]
    assert item1.name == 'Смартфон'


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_repr():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_str():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'


def test_add(position, phone1):
    assert position + phone1 == 11