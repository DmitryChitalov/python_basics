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


class Factory(ABC):
    @abstractmethod
    def calc_consumption(self):
        pass


class Clothes(Factory):
    _v = None
    _h = None

    @property
    def size(self):
        return self._v

    @size.setter
    def size(self, value):
        self._v = value
        self._h = None

    @property
    def height(self):
        return self._h

    @height.setter
    def height(self, value):
        self._h = value
        self._v = None

    def __init__(self, v=None, h=None):
        self._v = v
        self._h = h
        pass

    def calc_consumption(self):

        if self._v is None and self._h is None:
            raise Exception("'v' or 'h' are not set")

        res = 0
        if self._v is not None:
            res = self._v / 6.5 + 0.5
        if self._h is not None:
            res = self._h * 2 + 0.3

        return res

    def __add__(self, other):
        return self.calc_consumption() + other.calc_consumption()


coat = Clothes()
coat.size = 5.005

suite = Clothes()
suite.height = 10

total = coat + suite

print(f"Total consumption: {total}")
