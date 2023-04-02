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

class WorkingForm(ABC):
    @abstractmethod
    def fabric_calculation(self):
        pass

class Coat(WorkingForm):
    def __init__(self, v):
        self.v = v
    @property
    def fabric_calculation(self):
        V = self.v/6.5 + 0.5
        return f'Расход ткани на пальто = {V}'

class Suite(WorkingForm):
    def __init__(self, h):
        self.h = h
    @property
    def fabric_calculation(self):
        H = 2*self.h + 0.3
        return f'Расход ткани на костюм = {H}'
       
class TotalFabric(WorkingForm):
    def __init__(self, v, h):
        self.V = v
        self.H = h

    @property
    def fabric_calculation(self):
        all = (self.V/6.5 + 0.5) + (2*self.H + 0.3)
        return f'Общий расход ткани = {all}'

coat = Coat(130)
suite = Suite(1)
total = TotalFabric(130, 1)
print(suite.fabric_calculation)
print(coat.fabric_calculation)
print(total.fabric_calculation)
