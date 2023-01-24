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


class AbstractClothesClass(ABC):

    @abstractmethod
    def total_cloth_consumption(self):
        pass


class Clothes(AbstractClothesClass):

    clothes_types = ['Пальто', 'Костюм']

    def __init__(self, h, v):
        self.v = v
        self.h = h

    @property
    def suit_cloth_consumption(self):
        return self.h * 2 + 0.3

    @property
    def coat_cloth_consumption(self):
        return self.v / 6.5 + 0.5

    @property
    def total_cloth_consumption(self):
        return self.suit_cloth_consumption + self.coat_cloth_consumption


test_1 = Clothes(100, 100)
print(f'\
    Расход на костюм: {round(test_1.suit_cloth_consumption, 2)}\n\
    Расход на пальто: {round(test_1.coat_cloth_consumption, 2)}\n\
    Общий расход: {round(test_1.total_cloth_consumption, 2)}')

test_2 = Clothes(180, 52)
print(f'\
    Расход на костюм: {round(test_2.suit_cloth_consumption, 2)}\n\
    Расход на пальто: {round(test_2.coat_cloth_consumption, 2)}\n\
    Общий расход: {round(test_2.total_cloth_consumption, 2)}')