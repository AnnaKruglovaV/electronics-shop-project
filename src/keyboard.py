from src.item import Item


class MixLog:
    def __init__(self, name, price, quantity, language="EN"):
        super().__init__(name, price, quantity)
        self.language = language

    def __str__(self):
        return self.language

    def change_lang(self):
        if self.language == "EN":
            self.language = "RU"
        elif self.language == "RU":
            self.language = "EN"

        return self


class Keyboard(MixLog, Item):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)

    def __str__(self):
        return self.name
