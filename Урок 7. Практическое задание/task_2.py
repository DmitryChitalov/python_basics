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

from abc import abstractmethod, ABC

class MyClass(ABC):
    @abstractmethod
    def coat(self):
        pass
    @abstractmethod
    def suit(self):
        pass

class Clothes(MyClass):
    def __init__(self, el):
        self.el = el

    @property
    def coat(self):
        v = self.val / 6,5 + 0,5
        return v

    @property
    def suit(self):
        h = self.val * 2 + 0,3
        return h

a = Clothes(2)
print(f"Расход ткани на пальто: {a.coat}")
print(f"Расход ткани на костюм: {a.suit}")
print(f"Общий расход ткани: {a.coat + a.suit}")



