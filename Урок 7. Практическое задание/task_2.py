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
    collections = {
        'coat': lambda v: v / 6.5 + 0.5,
        'costume': lambda h: 2 * h + 0.3,
    }

    @abstractmethod
    def calc_from(self, what, size=0, height=0):
        return


class Clothes(AbstractClothes):
    def __init__(self):
        self.coat_expense = 0
        self.costume_expense = 0

    def calc_from(self, what, size=0, height=0):
        try:
            if what == 'coat':
                self.coat_expense = round(self.collections[what](size), 2)
                return self.coat_expense
            elif what == 'costume':
                self.costume_expense = round(self.collections[what](height), 2)
                return self.costume_expense
            return None
        except TypeError:
            return None

    @property
    def calc_all(self):
        return self.coat_expense + self.costume_expense

    def __str__(self):
        return f"{self.coat_expense}, {self.costume_expense}"


a = Clothes()
print(f"Расход ткани на пальто = {a.calc_from('coat', size=5)}")
print(f"Расход ткани на костюм = {a.calc_from('costume', height=10)}")
print(f"Общий расход ткани = {a.calc_all}")
