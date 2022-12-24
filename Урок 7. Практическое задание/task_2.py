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
    def expense_coat(self):
        pass

    @abstractmethod
    def expense_suit(self):
        pass

    def expense_all(self):
        pass


class Clothes(AbstractClothes):
    def __init__(self, coat, suit):
        self.coat = coat
        self.suit = suit

    def expense_coat(self):
        return round(self.coat / 6.5 + 0.5, 2)

    def expense_suit(self):
        return round(2 * self.suit + 0.3, 2)

    @property
    def expense_all(self):
        return round(self.expense_coat() + self.expense_suit(), 2)


c = Clothes(15, 40)
print(f'Расход ткани на пальто = {c.expense_coat()}')
print(f'Расход ткани на костюм = {c.expense_suit()}')
print(f'Общий расход ткани = {c.expense_all}')
