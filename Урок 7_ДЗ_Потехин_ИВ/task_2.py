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


# интерфейс,абстрактный класс
class AbstractClothes(ABC):
    @abstractmethod
    def get_coat_consumption(self):
        pass

    @abstractmethod
    def get_suit_consumption(self):
        pass

    @abstractmethod
    def get_total_consumption(self):
        pass


# интерфейс, класс Clothes
class Clothes(AbstractClothes):
    # атрибуты
    def __init__(self, v, h):
        self.v = v
        self.h = h

    # методы с использвоанием декоратора @property
    @property
    def get_coat_consumption(self):
        return self.v / 6.5 + 0.5

    @property
    def get_suit_consumption(self):
        return self.h * 2 + 0.3

    @property
    def get_total_consumption(self):
        return self.get_suit_consumption + self.get_coat_consumption


# клиентский код, создаем объект, вызываем меотоды, выводим на печать
clothes = Clothes(54, 1.9)
print(f'Расход ткани на пальто: {clothes.get_coat_consumption:.2f}')
print(f'Расход ткани на костюм: {clothes.get_suit_consumption:.2f}')
print(f'Общий расход ткани: {clothes.get_total_consumption:.2f}')
