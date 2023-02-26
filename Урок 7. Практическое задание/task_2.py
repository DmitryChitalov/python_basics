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
    def get_coat(self):
        pass

    @abstractmethod
    def get_suit(self):
        pass

    def get_all(self):
        pass


class Clothes:
    def __init__(self, v, h):
        self.v = v
        self.h = h
        self.coat = self.v / 6.5 + 0.5
        self.suit = self.h * 2 + 0.3

    def get_coat(self):
        return str(f'Расход ткани на пальто = {self.coat:.2f}')

    def get_suit(self):
        return str(f'Расход ткани на костюм = {self.suit:.2f}')

    @property
    def get_all(self):
        return str(f'Общий расход ткани = {self.coat + self.suit:.2f}')


clothes = Clothes(7, 42)

print(clothes.get_coat())
print(clothes.get_suit())
print(clothes.get_all)
