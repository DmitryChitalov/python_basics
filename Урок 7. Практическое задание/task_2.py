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
    
    @abstractmethod
    def get_consumption(self):
        pass

    @abstractmethod    
    def __str__(self):
        pass

class coat(Clothes):

    def __init__(self, size):
        self.size = size

    @property
    def get_consumption(self):
            return f'Расход ткани на пальто = {round(self.size / 6.5 + 0.5, 2)}'
    
    def __str__(self):
       return f'Размер пальто = {self.size}'
    

class jacket(Clothes):

    def __init__(self, height):
        self.height = height
        
    def __str__(self):
       return f'Высота костюма= = {self.height}'
    
    @property
    def get_consumption(self):
            consumption = round(self.height * 2 + 0.3, 2)
            return f'Расход ткани на костюм = {consumption}'
    
    def total(self, other):
         return f'Общий расход ткани = {round(self.height * 2 + 0.3 + other.size / 6.5 + 0.5, 2)}'

obj_c = coat(4)
obj_j = jacket(2)
print(obj_c.get_consumption)
print(obj_j.get_consumption)
print(obj_j.total(obj_c))