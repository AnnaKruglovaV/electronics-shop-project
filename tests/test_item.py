from src.item import Item
import pytest


@pytest.fixture
def position():
    return Item("Смартфон", 100, 1)


def test_item_init(position):
    assert position.name == "Смартфон"
    assert position.price == 100
    assert position.quantity == 1

def test_calculate_total_price(position):
    assert position.calculate_total_price() == 100


def test_first_task_item():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000

    Item.pay_rate = 0.8
    item1.apply_discount()

    assert item1.price == 8000.0
    assert item2.price == 20000