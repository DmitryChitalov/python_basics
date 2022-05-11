from abc import ABC, abstractmethod


class Abstract(ABC):
    @abstractmethod
    def get_coat_consump(self):
        pass

    @abstractmethod
    def get_suit_consump(self):
        pass

    def get_total_consump(self):
        pass


class Clothes(Abstract):
    def __init__(self, v, h):
        self.v = v
        self.h = h
        self.coat_consumption = self.v / 6.5 + 0.5
        self.suit_consumption = self.h * 2 + 0.3

    def get_coat_consump(self):
        return str(f'Расход на пальто = {self.coat_consumption:.1f}')

    def get_suit_consump(self):
        return str(f'Расход на костюм = {self.suit_consumption:.1f}')

    @property
    def get_total_consump(self):
        return str(f'Общий расход = {self.coat_consumption + self.suit_consumption:.1f}')


a = Clothes(10, 100)
print(a.get_coat_consump())
print(a.get_suit_consump())
print(a.get_total_consump)
