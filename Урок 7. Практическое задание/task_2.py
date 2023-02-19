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
    def consumption(self):
        pass

class Coat(Clothes):
    def __init__(self, size):
        self.size = size
    def consumption(self):
        return self.size / 6.5 + 0.5

    def __str__(self):
        return f'Расход ткани на пальто: {self.consumption()}'

class Suit(Clothes):
    def __init__(self, height):
        self.height = height
    def consumption(self):
        return self.height * 2 + 0.3

    def __str__(self):
        return f'Расход ткани на костюм: {self.consumption()}'

coats = Coat(5)
suits = Suit(10)
print(coats)
print(suits)
print(coats.consumption() + suits.consumption())
