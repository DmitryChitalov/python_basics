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

"""
Выполенине! Емельяненко А.А.
"""

from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def __init__(self, name):
        pass

    @abstractmethod
    def tissue_consumption(self):
        pass

    def __add__(self, other):
        return self.tissue_consumption + other.tissue_consumption


class Palto(Clothes):
    def __init__(self, the_size, name='default'):
        super().__init__(name)
        self.name, self.the_size = name, the_size

    @property
    def tissue_consumption(self):
        return self.the_size / 2 + 45.5


class Hoff(Clothes):
    def __init__(self, height, name='default'):
        super().__init__(name)
        self.name, self.height = name, height

    @property
    def tissue_consumption(self):
        return 2 * self.height + 0.3


palto = Palto(23)
print(f'Расход ткани на пальто: {palto.tissue_consumption:.2f}')

hoff = Hoff(23, name='hoff')
print(f'Расход ткани на брюки: {hoff.tissue_consumption:.2f}')

print(f'Общий расход ткани: {palto + hoff:.2f}')
