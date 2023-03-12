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
    def __init__(self, size, height):
        self.size = size
        self.height = height

    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        super().__init__(size, None)

    def fabric_consumption(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, height):
        super().__init__(None, height)

    def fabric_consumption(self):
        return self.height * 2 + 0.3


class TotalFabricConsumption:
    def __init__(self, clothes_list):
        self.clothes_list = clothes_list

    @property
    def total_fabric_consumption(self):
        return sum(
            [clothes.fabric_consumption() for clothes in self.clothes_list])

coat = Coat(50)
suit = Suit(1.8)

print(f"Расход ткани на пальто = {coat.fabric_consumption():.2f}")
print(f"Расход ткани на костюм = {suit.fabric_consumption():.2f}")

total = TotalFabricConsumption([coat, suit])
print(f"Общий расход ткани = {total.total_fabric_consumption:.2f}")
