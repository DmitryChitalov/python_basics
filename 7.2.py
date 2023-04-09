from abc import ABC, abstractmethod


class Clothes(ABC):
    name: str

    def __init__(self, name: str):
        self.name = name

    @property
    @abstractmethod
    def calculate(self) -> float:
        pass


class Coat(Clothes):
    _size: float

    def __init__(self, name: str, size: float):
        super().__init__(name)
        self._size = size

    @property
    def calculate(self) -> float:
        return self._size / 6.5 + 0.5


class Suit(Clothes):
    _height: float

    def __init__(self, name: str, height: float):
        super().__init__(name)
        self._height = height

    @property
    def calculate(self) -> float:
        return 2 * self._height + 0.3


coat = Coat('Пальто', 3)
print(coat.calculate)

suit = Suit('Костюм', 1.8)
print(suit.calculate)