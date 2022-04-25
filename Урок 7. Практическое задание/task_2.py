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
    def get_coat(self):
        pass

    @abstractmethod
    def get_suit(self):
        pass

    def get_total(self):
        pass


class Clothes(AbstractClothes):
    def __init__(self, v, h):
        self.v = v
        self.h = h

    @property
    def get_coat(self):
        return self.v / 6.5 + 0.5

    @property
    def get_suit(self):
        return 2 * self.h + 0.3

    @property
    def get_total(self):
        return self.get_suit + self.get_coat


my_cloth = Clothes(2, 3)
print(f"Расход ткани на пальто - {my_cloth.get_coat}")
print(f"Расход ткани на костюм - {my_cloth.get_suit}")
print(f"Общий расход ткани - {my_cloth.get_total}")
