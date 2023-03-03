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
# pylint: disable=missing-class-docstring, missing-function-docstring, invalid-overridden-method

from abc import ABC, abstractmethod


class AbstractClothes(ABC):
    @abstractmethod
    def get_coat_consumption(self):
        pass

    @abstractmethod
    def get_suit_consumption(self):
        pass

    def get_total_consumption(self):
        pass


class Clothes(AbstractClothes):
    def __init__(self, v, h):
        self.v = v
        self.h = h
        self.coat_consumption = self.v / 6.5 + 0.5
        self.suit_consumption = self.h * 2 + 0.3

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
