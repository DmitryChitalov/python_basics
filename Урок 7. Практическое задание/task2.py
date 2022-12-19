from abc import ABC, abstractmethod

class ABCClothes(ABC):

    def __init__(self, name, size, height):
        self.name = name
        self.height = height
        self.size = size

    def name(self):
        return self.name

    @abstractmethod
    def calculation(self):
        pass

class Clothes(ABCClothes):
    def __init__(self, name, size, height):
        self.name = name
        self.height = height
        self.size = size

    def calculation(self):
        self.a = self.height / 6.5 + 0.5
        self.b = 2 * self.size + 0.3
        return f"Для костюма: {self.a:.2f}. Для пальто: {self.b:.2f}"

    @property
    def result(self):
        c = self.a + self.b
        return f"Полные затраты на одежду: {c:.2f}"

class Coat(ABCClothes):
    pass

class Suit(ABCClothes):
    pass

a = Clothes("Одежда", 3.2, 32)
print(a.calculation())
print(a.result)
