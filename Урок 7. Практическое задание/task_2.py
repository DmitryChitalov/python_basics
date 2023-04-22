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
    def __init__(self, params):
        self.params = params

    @abstractmethod
    def fabric_consumption(self):
        pass

    def get_params(self):
        return self.params

    def __add__(self, other):
        return self.fabric_consumption() + other.fabric_consumption()


class Coat(Clothes):
    @property
    def params(self):
        return self.__params

    @params.setter
    def params(self, params):
        if params > 100:
            self.__params = 100
        elif params < 13:
            self.__params = 13
        else:
            self.__params = params

    def fabric_consumption(self):
        return (self.get_params() / 6.5) + 0.5


class Suit(Clothes):

    @property
    def params(self):
        return self.__params

    @params.setter
    def params(self, params):
        if params > 2.2:
            self.__params = 2.2
        elif params < 1.3:
            self.__params = 1.3
        else:
            self.__params = params

    def fabric_consumption(self):
        return 2 * self.get_params() + 0.3


coat = Coat(58)
suit = Suit(1.83)

print(f'Расход ткани на пальто = {round(coat.fabric_consumption(), 2)}')
print(f'Расход ткани на костюм = {round(suit.fabric_consumption(), 2)}')
print(f'Общий расход ткани = {round((coat + suit), 2)}')
