from abc import ABC, abstractmethod, abstractproperty

class Clothes(ABC):
    def __add__(self, other):
        return (f' Общий расход ткани {round(self.exp + other.exp)}')
    @abstractmethod
    def exp(self):
        pass

class Coat(Clothes):
    def __init__(self, V):
        self.V = float(V)
    @property
    def exp(self):
        return round(self.V / 6.5 + 0.5)

class Suit(Clothes):
    def __init__(self, H):
        self.H = float(H)
    @property
    def exp(self):
        return round(2 * self.H + 0.3)

coat_1 = Coat(40)
suit_1 = Suit(15)

print(coat_1.exp)
print(suit_1.exp)
print(coat_1 + suit_1)
