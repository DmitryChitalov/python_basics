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


class AClothes(ABC):
    @abstractmethod
    def g_coat_expand(self):
        pass

    @abstractmethod
    def g_suit_expand(self):
        pass

    def g_total_expand(self):
        pass


class Clothes(AClothes):
    def __init__(self, v, h):
        self.v = v
        self.h = h
        self.coat_expand = self.v / 6.5 + 0.5
        self.suit_expand = self.h * 2 + 0.3

    def g_coat_expand(self):
        return str(f"Расход ткани на пальто = {self.coat_expand:.2f}")

    def g_suit_expand(self):
        return str(f"Расход ткани на костюм = {self.suit_expand:.2f}")

    @property
    def g_total_expand(self):
        return str(f"Общий расход ткани = {self.coat_expand + self.suit_expand:.2f}")


clothes = Clothes(12, 33)

print(clothes.g_coat_expand())
print(clothes.g_suit_expand())
print(clothes.g_total_expand)
