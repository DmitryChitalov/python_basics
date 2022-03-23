"""
Задание 2.

Реализовать проект расчета суммарного расхода ткани на производство одежды.

Единственный класс этого проекта — одежда (класс Clothes).

К типам одежды в этом проекте относятся пальто и костюм.

У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: v и h,
соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (v/6.5 + 0.5),
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
    def __init__(self, parameter):
        self.parameter = parameter

    @property
    def total_consumption(self):
        return f'Fabric consumption is ' \
               f'{self.parameter / 6.5 + 0.5 + 2 * self.parameter + 0.3 :.2f}'

    @abstractmethod
    def abstract(self):
        return 'Abstract'


class Coat(Clothes):
    def consumption(self):
        return f'To make a coat you need ' \
               f'{self.parameter / 6.5 + 0.5 :.2f} fabric'

    def abstract(self):
        return 'Abstract 2'


class Costume(Clothes):
    def consumption(self):
        return f'To make a costume you need ' \
               f'{2 * self.parameter + 0.3 :.2f} fabric'

    def abstract(self):
        pass


coat = Coat(500)
costume = Costume(55)
print(coat.consumption())
print(costume.consumption())
