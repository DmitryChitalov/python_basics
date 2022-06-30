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


class AbsCloth(ABC):
    @abstractmethod
    def calc_expense_coat(self):
        pass

    @abstractmethod
    def calc_expense_costume(self):
        pass

    def calc_expense_total(self):
        pass


class Clothes(AbsCloth):
    def __init__(self, v, h):
        self.v = v
        self.h = h
        self.expense_coat = self.v / 6.5 + 0.5
        self.expense_costume = self.h * 2 + 0.3

    def calc_expense_coat(self):
        return str(f'Подсчет расхода ткани на пальто >>> {self.expense_coat:.2f} кв.м')

    def calc_expense_costume(self):
        return str(f'Подсчет расхода ткани на костюм >>> {self.expense_costume:.2f} кв.м')

    @property
    def calc_expense_total(self):
        return str(f'Общий подсчет расхода ткани >>> {self.expense_coat + self.expense_costume:.2f} кв.м')


clothes = Clothes(5, 10)

print(clothes.calc_expense_coat())
print(clothes.calc_expense_costume())
print(clothes.calc_expense_total)
