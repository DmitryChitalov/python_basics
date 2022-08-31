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


class MyAbstrClass(ABC):
    @abstractmethod
    def fabric_consumption(self):
        pass


class Clothes(MyAbstrClass):
    def __init__(self, cloth_type, size):
        self.cloth_type = cloth_type
        self.size = size
        self.__prize = "500$"

    def fabric_consumption(self):

        if self.cloth_type == "coat":
            self.__prize = "1000$"
            return self.size / 6.5 + 0.5
        elif self.cloth_type == "suit":
            self.__prize = "2000$"
            return 2 * self.size + 0.3
        else:
            return "Указан неправильный тип одежды"

    @property
    def prize(self):
        return self.__prize


coat = Clothes("coat", 5)
suit = Clothes("suit", 10)
print(f"Расход ткани на пальто = {round(coat.fabric_consumption(), 2)}")
print(f"Расход ткани на костюм {round(suit.fabric_consumption(), 2)}")
print(f"Общий расход ткани = {round(coat.fabric_consumption(), 2) + round(suit.fabric_consumption(), 2)}")
print(coat.prize)
