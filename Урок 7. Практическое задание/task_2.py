from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def fabric_consumption(self):
        return round(self.size / 6.5 + 0.5, 2)


class Suit(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def fabric_consumption(self):
        return round(2 * self.height + 0.3, 2)


class TotalFabricConsumption:
    def __init__(self, clothes):
        self.clothes = clothes

    def total_fabric_consumption(self):
        return round(sum([item.fabric_consumption for item in self.clothes]), 2)


coat = Coat(52)
suit = Suit(1.8)

print(f"Расход ткани на пальто = {coat.fabric_consumption}")
print(f"Расход ткани на костюм = {suit.fabric_consumption}")

total_consumption = TotalFabricConsumption([coat, suit])
print(f"Общий расход ткани = {total_consumption.total_fabric_consumption()}")

