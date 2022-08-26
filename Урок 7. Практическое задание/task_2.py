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
    def __init__(self, param):
        self.param = param

    @property
    def consumption(self):
        return f'Общий расход ткани = {self.param / 6.5 + 0.5 + 2 * self.param + 0.3 :.2f}'

    @abstractmethod
    def abstract(self):
        return "Ошибка!"


class Coat(Clothes):
    def consumption_coat(self):
        return f'Расход ткани на пальто: {self.param / 6.5 + 0.5 :.2f}'

    def abstract(self):
        "Ошибка!"


class Costume(Clothes):
    def consumption_costume(self):
        return f'Расход ткани на костюм: {2 * self.param + 0.3 :.2f}'

    def abstract(self):
        pass


coat = Coat(8)
costume = Costume(7)
print(f'{costume.consumption} на костюм')
print(f'{coat.consumption} на пальто')
print(costume.consumption_costume())
print(coat.consumption_coat())
