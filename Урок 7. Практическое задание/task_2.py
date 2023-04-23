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


class MyAbsClass(ABC):
    @abstractmethod
    def volume_calc(self):
        pass


class Clothes(MyAbsClass):

    def __init__(self):
        self.clothes_type = ""

    def __setattr__(self, attr, value):
        if attr == "clothes_type":
            if value == "suit" or value == "coat":
                self.__dict__[attr] = value
            else:
                pass
        elif (self.clothes_type == "coat" and attr == "v") or (self.clothes_type == "suit" and attr == "h"):
            self.__dict__[attr] = value
        else:
            pass

    @property
    def volume_calc(self):
        if self.clothes_type == "coat":
            return f"Расход ткани на пальто = {self.v / 6.5 + 0.5}"
        elif self.clothes_type == "suit":
            return f"Расход ткани на костюм = {self.h * 2 + 0.3}"

    def __add__(self, other):
        vol1 = 0
        vol2 = 0
        if self.clothes_type == "coat":
            vol1 = self.v / 6.5 + 0.5
        elif self.clothes_type == "suit":
            vol1 = self.h * 2 + 0.3
        if other.clothes_type == "coat":
            vol2 = other.v / 6.5 + 0.5
        elif other.clothes_type == "suit":
            vol2 = other.h * 2 + 0.3
        return f"Суммарный расход ткани = {vol1 + vol2}"


obj_1 = Clothes()
obj_2 = Clothes()
obj_1.clothes_type = "coat"
obj_2.clothes_type = "suit"
obj_1.v = 50
obj_2.h = 1.8
print(obj_1.volume_calc)
print(obj_2.volume_calc)
res_vol = obj_1 + obj_2
print(res_vol)
