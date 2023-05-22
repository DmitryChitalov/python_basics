from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def consumption(self):
        pass

class Coat(Clothes):
    @property
    def consumption(self):
        return f'Всего для пошива пальто нужно: {self.param / 6.5 + 0.5 :.2f} метров ткани'

class Costume(Clothes):
    @property
    def consumption(self):
        return f'Всего для пошива костюма нужно: {2 * self.param + 0.3 :.2f} метров ткани'

coat = Coat(100)
costume = Costume(50)

print(coat.consumption)
print(costume.consumption)