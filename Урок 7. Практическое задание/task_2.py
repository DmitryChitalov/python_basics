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


class ClothesAbstract(ABC):

    @abstractmethod
    def total_consumption(self):
        pass


class Clothes(ClothesAbstract):
    def __init__(self, size: int, height: float):
        self._v = size
        self._h = height

    @property
    def total_consumption(self):
        return self.coat_consumption + self.suit_consumption

    @property
    def coat_consumption(self):
        return self._v / 6.5 + 0.5

    @property
    def suit_consumption(self):
        return self._h * 2 + 0.3

    def __str__(self):
        return f'''
Расход ткани на пальто - {self.coat_consumption:.2f}
Расход ткани на костюм - {self.suit_consumption:.2f}
Общий расход ткани - {self.total_consumption:.2f}
'''


roman = Clothes(size=52, height=1.8)
ivan = Clothes(size=48, height=1.65)
print(roman)
print(ivan)
