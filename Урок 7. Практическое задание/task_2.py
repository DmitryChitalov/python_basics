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
from typing import Any


class AbstractClothes(ABC):
    """ Интерфейс одежды """

    @property
    @abstractmethod
    def issue_req(self):
        pass

    """ Общая размерность одежды """

    @property
    @abstractmethod
    def measure(self):
        pass

    @abstractmethod
    def _calc_issue_req(self):
        pass


""" Одежда """


class Clothes(AbstractClothes):
    _clothes = []

    def __init__(self, name: str, measuring: any):
        self.name = name
        self._measure = measuring
        self._issue_req = None
        self._clothes.append(self)

    def _calc_issue_req(self):
        raise NotImplemented

    @property
    def issue_req(self) -> float:
        if not self._issue_req:
            self._calc_issue_req()

        return self._issue_req

    @property
    def measure(self) -> any:
        return self._measure

    @measure.setter
    def measure(self, measuring: any):
        self._measure = measuring
        self._issue_req = None

    @property
    def total_issue_req(self):
        return sum([item.issue_req for item in self._clothes])


class Coat(Clothes):
    def _calc_issue_req(self):
        self._issue_req = round(self.measure / 6.5 + 0.5, 2)

    @property
    def c_size(self):
        return self.measure

    @c_size.setter
    def c_size(self, size: any):
        self.measure = size

    def __str__(self):
        return f"Для пошива пальто {self.measure} размера " \
               f"требуется {self.issue_req} кв. метров ткани"


class Suit(Clothes):
    def _calc_issue_req(self):
        self._issue_req = round(2 * self.measure * 0.01 + 0.3, 2)

    @property
    def s_size(self) -> any:
        return self.measure

    @s_size.setter
    def s_size(self, height: any):
        self.measure = height

    def __str__(self):
        return f"Для пошива костюма на рост {self.measure} см. " \
               f"требуется {self.issue_req} кв. метров ткани"


if __name__ != '__main__':
    pass
else:

    coat = Coat('Пальто от Шанель', 0)
    # print(coat)
    coat.c_size = 34
    print('Пальто от Шанель: ', coat)

    suit = Suit('Костюм от Бордо', 0)
    # print(suit)
    suit.s_size = 175
    print('Костюм от Бордо: ', suit)


