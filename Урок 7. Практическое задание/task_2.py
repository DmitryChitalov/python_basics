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
class MyAbstractClass(ABC):
    @abstractmethod
    def suit(self):
        pass

    @abstractmethod
    def coat(self):
        pass


class Clothes:

    def __init__(self, val):
        self.coat_textile = val / 6.5 + 0.5
        self.suit_textile = 2 * val + 0.3

    @property
    def suit(self):
        return "Расход ткани на костюм = " + str(self.suit_textile)

    @property
    def coat(self):
        return f"Расход ткани на костюм = {self.coat_textile:.2f}"

    @property
    def total(self):
        return f"Общий расход ткани = {(self.suit_textile + self.coat_textile):.2f}"


obj = Clothes(2)
print(obj.suit)
print(obj.coat)
print(obj.total)