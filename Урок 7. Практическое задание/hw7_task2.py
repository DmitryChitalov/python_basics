from abc import ABC, abstractmethod


class AbsClothes(ABC):
    @abstractmethod
    def coat_fab(self):
        pass

    @abstractmethod
    def suit_fab(self):
        pass

    @abstractmethod
    def all_fab(self):
        pass


class Clothes(AbsClothes):
    def __init__(self, v, h):
        self.v = v
        self.h = h

    def coat_fab(self):
        return str(f"Расход ткани на пальто: {self.v / 6.5 + 0.5}")

    def suit_fab(self):
        return str(f"Расход ткани на костюм: {self.h * 2 + 0.3}")

    @property
    def all_fab(self):
        return f"Расход ткани на пальто и костюм: {(self.v / 6.5 + 0.5) + (self.h * 2 + 0.3)}"


c = Clothes(5, 10)
print(c.coat_fab())
print(c.suit_fab())
print(c.all_fab)