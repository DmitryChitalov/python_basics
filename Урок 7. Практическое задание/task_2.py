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
    def fabric_waste(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def fabric_waste(self):
        return round(self.size / 6.5 + 0.5, 2)


class Suit(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def fabric_waste(self):
        return round(2 * self.height + 0.3, 2)


coat = Coat(11)
suit = Suit(29)
total_fabric_waste = round(coat.fabric_waste + suit.fabric_waste, 2)

print(f'Расход ткани на пальто: {coat.fabric_waste}')
print(f'Расход ткани на костюм: {suit.fabric_waste}')
print(f'Общий расход ткани на изделия: {total_fabric_waste}')
