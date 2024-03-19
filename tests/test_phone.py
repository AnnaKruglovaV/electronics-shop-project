import pytest
from src.phone import Phone


@pytest.fixture
def phone1():
    """
    Экземпляр класса в фикстуре
    """
    return Phone("IPhone", 30000, 10, 2)


def test_1(phone1):
    """
    Тест метода init
    """
    assert phone1.name == "IPhone"
    assert phone1.price == 30000
    assert phone1.quantity == 10
    assert phone1.number_of_sim == 2
