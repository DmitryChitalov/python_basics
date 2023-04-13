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


class MyClass(ABC):
    @abstractmethod
    def calculate_coat(self):
        pass

    @abstractmethod
    def calculate_costume(self):
        pass


class Clothes(MyClass):
    def __init__(self, number):
        self.number = number

    @property
    def calculate_coat(self):
        return round(self.number/6.5 + 0.5, 2)

    @property
    def calculate_costume(self):
        return round(2*self.number + 0.3, 2)


a = Clothes(12)
print(f"Расход ткани на пальто: {a.calculate_coat}")
print(f"Расход ткани на костюм: {a.calculate_costume}")
print(f"Общий расход ткани: {round(a.calculate_coat + a.calculate_costume, 2)}")
