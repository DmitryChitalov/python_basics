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
    def tissue_required(self):
        pass

    @property
    @abstractmethod
    def measuring(self):
        """ Общая размерность одежды """
        pass

    @abstractmethod
    def _calc_tissue_required(self):
        pass


class Clothes(AbstractClothes):
    _clothes = []

    """ Одежда """
    def __init__(self, name: str, measuring: Any):
        self.name = name
        self._measuring = measuring
        self._tissue_required = None

        self._clothes.append(self)

    def _calc_tissue_required(self):
        raise NotImplemented

    @property
    def tissue_required(self) -> float:
        """ Расход ткани """
        if not self._tissue_required:
            self._calc_tissue_required()

        return self._tissue_required

    @property
    def measuring(self) -> Any:
        """ Узнать размер """
        return self._measuring

    @measuring.setter
    def measuring(self, measuring: Any):
        """ Установить новый размер пальто """
        self._measuring = measuring
        self._tissue_required = None

    @property
    def total_tissue_required(self):
        """ Ткани на всю одежду """
        return sum([item.tissue_required for item in self._clothes])


class Coat(Clothes):
    """ Пальто """
    def _calc_tissue_required(self):
        """ посчитать расход ткани для пальто """
        self._tissue_required = round(self.measuring / 6.5 + 0.5, 2)

    @property
    def V(self) -> Any:
        """ Узнать размер пальто """
        return self.measuring

    @V.setter
    def V(self, size: Any):
        """ Установить новый размер пальто """
        self.measuring = size

    def __str__(self):
        return f"Для пошива пальто {self.measuring} размера " \
               f"требуется {self.tissue_required} кв. метров ткани"


class Suit(Clothes):
    """ Костюм """
    def _calc_tissue_required(self):
        """ посчитать расход ткани для костюма """
        self._tissue_required = round(2 * self.measuring * 0.01 + 0.3, 2)

    @property
    def H(self) -> Any:
        """ Узнать размер костюма """
        return self.measuring

    @H.setter
    def H(self, height: Any):
        """ Установить новый размер костюма """
        self.measuring = height

    def __str__(self):
        return f"Для пошива костюма на рост {self.measuring} см. " \
               f"требуется {self.tissue_required} кв. метров ткани"


if __name__ == '__main__':
    coat = Coat('Пальто', 10)
    print(coat)

    suit = Suit('Костюм', 200)
    print(suit)

    print("Общий расход ткани ", coat.total_tissue_required, "кв. метров ткани")


