from abc import ABC, abstractmethod

class AbstractClothes(ABC):
    @abstractmethod
    def get_coat_consumption(self):
        pass

    @abstractmethod
    def get_suit_consumption(self):
        pass

    @abstractmethod
    def get_total_consumption(self):
        pass


class Clothes(AbstractClothes):
    def __init__(self, v, h):
        self.v = v
        self.h = h
        self.coat_consumption = self.v / 6.5 +0.5
        self.suit_consumption = self.h *2 + 0.3

    def get_coat_consumption(self):
        return str(f'Расход ткани на пальто = {self.coat_consumption:.2f}')

    def get_suit_consumption(self):
        return str(f'Расход ткани на костюм = {self.suit_consumption:.2f}')

    @property
    def get_total_consumption(self):
        return str(f'Общий расход ткани = {self.coat_consumption + self.suit_consumption:.2f}')

clothes = Clothes(5, 10)

print(clothes.get_coat_consumption())
print(clothes.get_suit_consumption())
print(clothes.get_total_consumption)