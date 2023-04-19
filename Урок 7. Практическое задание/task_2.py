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
    @property
    @abstractmethod
    def tissue_required(self):
        pass

    @property
    @abstractmethod
    def measuring(self):
        pass

    @abstractmethod
    def _calc_tissue_required(self):
        pass


class Clothes(AbstractClothes):
    _clothes = []

    def __init__(self, name: str, measuring: Any):
        self.name = name
        self._measuring = measuring
        self._tissue_required = None

        self._clothes.append(self)

    def _calc_tissue_required(self):
        raise NotImplemented

    @property
    def tissue_required(self) -> float:
        if not self._tissue_required:
            self._calc_tissue_required()

        return self._tissue_required

    @property
    def measuring(self) -> Any:
        return self._measuring

    @measuring.setter
    def measuring(self, measuring: Any):
        self._measuring = measuring
        self._tissue_required = None

    @property
    def total_tissue_required(self):
        return sum([item.tissue_required for item in self._clothes])


class Coat(Clothes):
    def _calc_tissue_required(self):
        self._tissue_required = round(self.measuring / 6.5 + 0.5, 2)

    @property
    def v(self) -> Any:
        return self.measuring

    @v.setter
    def v(self, size: Any):
        self.measuring = size

    def __str__(self):
        return f'Расход ткани на пальто размера {self.measuring} =  {self.tissue_required}'


class Suit(Clothes):
    def _calc_tissue_required(self):
        self._tissue_required = round(2 * self.measuring + 0.3, 2)

    @property
    def h(self) -> Any:
        return self.measuring

    @h.setter
    def h(self, height: Any):
        self.measuring = height

    def __str__(self):
        return f'Расход ткани на костюм роста {self.measuring} = {self.tissue_required}'


if __name__ == '__main__':
    coat = Coat('Пальто', 58)
    print(coat)
    coat.v = 46
    print(coat)

    suit = Suit('Костюм', 178)
    print(suit)
    suit.h = 200
    print(suit)

    print(coat.total_tissue_required)
    print(suit.total_tissue_required)