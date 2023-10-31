from src.item import Item


class KeyboardLayoutMixin:
    def __init__(self):
        self.__language = "EN"

    def change_lang(self):
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"
            
    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, value):
        if value not in ["EN", "RU"]:
            raise AttributeError("Скажем другому языку - НЕ СЕГОДНЯ!")
        self._language = value


class Keyboard(Item, KeyboardLayoutMixin):
    def __init__(self, name, price, quantity):
        Item.__init__(self, name, price, quantity)
        KeyboardLayoutMixin.__init__(self)

    def __str__(self):
        return self.name
