"""
Задание 2.

Реализовать проект расчета суммарного расхода ткани на производство одежды.

Единственный класс этого проекта — одежда (класс Clothes).

К типам одежды в этом проекте относятся пальто и костюм.

У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: v и h, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (v/6.5 + 0.5),
для костюма (2*h + 0.3). Проверить работу этих методов на реальных данных.

Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать
абстрактный класс для единственного класса проекта,
проверить на практике работу декоратора @property

Пример:
Расход ткани на пальто = 1.27
Расход ткани на костюм = 20.30
Общий расход ткани = 21.57

Два класса: абстрактный и Clothes
"""

from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def calculate_consumption(self):
        raise NotImplementedError


class Coat(Clothes):
    size: int

    def __init__(self, size: int):
        self.size = size

    @property
    def calculate_consumption(self):
        return round(self.size / 6.5 + 0.5, 2)


class Suit(Clothes):
    _height: float

    def __init__(self, height: float):
        self.height = height

    @property
    def calculate_consumption(self):
        return round(2 * self.height + 0.3, 2)


class Composite(Clothes):
    _children: list

    def __init__(self, children: list):
        self._children = children

    @property
    def calculate_consumption(self):
        total_consumption = 0
        for item in self._children:
            total_consumption += item.calculate_consumption
        return total_consumption


coat = Coat(56)
suit = Suit(1.8)
composite = Composite([coat, suit])

print(f'The cloth consumption for coat equals: {coat.calculate_consumption} m')
print(f'The cloth consumption for suit equals: {suit.calculate_consumption} m')
print(f'The total cloth consumption for all clothes equals: {composite.calculate_consumption}')
