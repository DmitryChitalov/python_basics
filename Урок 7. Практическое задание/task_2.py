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


class IClothes(ABC):
    @abstractmethod
    def fabric_consumption_coat(self):
        pass

    @abstractmethod
    def fabric_consumption_suit(self):
        pass

    @abstractmethod
    def total_consumption(self):
        pass


class Clothes(IClothes):

    def __init__(self, v, h):
        self.v = v
        self.h = h

    @property
    def fabric_consumption_coat(self):
        return self.v / 6.5 + 0.5

    @property
    def fabric_consumption_suit(self):
        return 2 * self.h + 0.3

    @property
    def total_consumption(self):
        return self.fabric_consumption_suit + self.fabric_consumption_coat

    def __str__(self):
        consumption_coat = f'Расход ткани на пальто = {self.fabric_consumption_coat:.2f}'
        consumption_suit = f'Расход ткани на костюм = {self.fabric_consumption_suit:.2f}'
        total_consumption = f'Общий расход ткани = {self.total_consumption:.2f}'
        return f'{consumption_coat}\n{consumption_suit}\n{total_consumption}'


clothes = Clothes(10, 15)
print(clothes)
