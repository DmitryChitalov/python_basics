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

    def __init__(self, atribut):
        self.atribut = atribut

    @abstractmethod
    def expense(self):
        pass

    def __add__(self, other):
        return f'Общий расход ткани = {self.atribut + other.atribut}'


class Coat(Clothes):

    @property
    def expense(self):
        self.atribut = round((self.atribut / 6.5 + 0.5), 2)
        print(f'Необходимо на пальто = {self.atribut}м.')
        return self.atribut


class Costume(Clothes):

    @property
    def expense(self):
        self.atribut = round((self.atribut * 2 + 0.3), 2)
        print(f'Необходимо на костюм = {self.atribut}м.')
        return self.atribut


coat = Coat(15)
costume = Costume(20)

expense_update = coat.expense + costume.expense
print(f'Общий расход ткани = {expense_update}м.')
