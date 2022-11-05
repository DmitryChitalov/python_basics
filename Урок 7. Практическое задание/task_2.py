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


class AbstractClothes(ABC):

    @abstractmethod
    def cost_coat(self):
        pass

    @abstractmethod
    def cost_suit(self):
        pass

    @abstractmethod
    def total_cost(self):
        pass


class Clothes(AbstractClothes):
    def __init__(self, v, h):
        self.v = v
        self.h = h
        self.r_coat = v / 6.5 + 0.5
        self.r_suit = 2 * h + 0.3

    def cost_coat(self):
        return str(f'Расход ткани на пальто : {self.r_coat}')

    def cost_suit(self):
        return str(f'Расход ткани на костюм : {self.r_suit}')

    @property
    def total_cost(self):
        res = self.r_suit + self.r_coat
        return str(f'Общий расход ткани : {res}')


coat1 = Clothes(48, 10)
print(coat1.cost_suit())
print(coat1.cost_coat())
print(coat1.total_cost)
