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
    def coat(self):
        pass

    @abstractmethod
    def suit(self):
        pass


class Clothes(AbstractClothes):

    def __init__(self, v, h):
        self.v = v
        self.h = h

    def coat(self):
        return round(self.v / 6.5 + 0.5, 2)

    def suit(self):
        return round(2 * self.h + 0.3, 2)

    @property
    def total_consumption(self):
        return self.coat() + self.suit()


clothes = Clothes(5, 9)
print(f'Расход ткани на пальто = {clothes.coat()}')
print(f'Расход ткани на костюм = {clothes.suit()}')
print(f'Общий расход ткани = {clothes.total_consumption}')
