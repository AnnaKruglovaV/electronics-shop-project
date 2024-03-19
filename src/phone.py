from src.item import Item


class Phone(Item):
    """ Дочерний класс, который содержит в себе все аотибуты класса Item
        и дополнительный атрибут, содержащий количество поддерживаемых сим-карт"""
    def __init__(self, name, price, quantity, number_of_sim) -> None:
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __repr__(self):
        """ Метод, который выводит ифнормацию для разработиков """
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"
