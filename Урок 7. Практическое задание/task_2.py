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

class Clothes:
    def __init__(self, v, h):
        self.v = v
        self.h = h

    @property
    def calc_coat(self):
        return self.v / 6.5 + 0.5

    @property
    def calc_costume(self):
        return 2 * self.h + 0.3

    @property
    def calc_all(self):
        return self.calc_coat + self.calc_costume

f = Clothes(5, 1)
print(f'Расход ткани на пальто = {f.calc_coat :.2f}')
print(f'Расход ткани на костюм = {f.calc_costume :.2f}')
print(f'Общий расход ткани = {f.calc_all :.2f}')


# Два класса: абстрактный и Clothes
from abc import ABC, abstractmethod

class Clothe(ABC):

    def __init__(self, param):
        self.param = param


    @property
    def consumption(self):
        pass


class Coat(Clothe):
    @property
    def consumption(self):
        return f'Расход ткани на пальто: {self.param / 6.5 + 0.5 :.2f} м ткани'



class Costume(Clothe):
    @property
    def consumption(self):
        return f'Расход ткани на костюм: {2 * self.param + 0.3 :.2f} м ткани'



coat = Coat(5)
costume = Costume(1)
print(coat.consumption)
print(costume.consumption)
