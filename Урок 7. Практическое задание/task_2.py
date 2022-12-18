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


class AbstractClothes(ABC):     # создаём абстрактный класс
    @abstractmethod
    def coat_fabric_consumption(self):  # создаём абстрактный метод
        pass

    @abstractmethod
    def suit_fabric_consumption(self):  # создаём абстрактный метод
        pass


class Clothes(AbstractClothes):     # создаём класс на основе абстрактного

    def __init__(self, s):
        self.s = s

    @property                               # @property позволяет работать с методом  как с атрибутом
    def coat_fabric_consumption(self):      # определяем метод
        return self.s / 6.5 + 0.5

    @property
    def suit_fabric_consumption(self):
        return 2 * self.s + 0.3


coat = Clothes(20)
suit = Clothes(20)
# обращаемся к методу coat_fabric_consumption и suit_fabric_consumption, как к атрибуту
print('Расход ткани на пальто =', coat.coat_fabric_consumption)
print('Расход ткани на костюм =', suit.suit_fabric_consumption)
print('Общий расход ткани =', coat.coat_fabric_consumption + suit.suit_fabric_consumption)
