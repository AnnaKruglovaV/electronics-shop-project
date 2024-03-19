import pytest
from src.keyboard import Keyboard


@pytest.fixture()
def keyboard1():
    """
    Экземпляр класса в фикстуре
    """
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_change_lang(keyboard1):
    """
    Тесты функции change_lang
    """
    keyboard1.change_lang()
    assert str(keyboard1.language) == "RU"
    keyboard1.change_lang().change_lang()
    assert str(keyboard1.language) == "RU"


def test_str(keyboard1):
    """
    Тест метода str
    """
    assert str(keyboard1) == "Dark Project KD87A"
    assert str(keyboard1.language) == "EN"
