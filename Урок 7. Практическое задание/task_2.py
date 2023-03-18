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


class AbstractClothes(ABC):
    @abstractmethod
    def coat_consumption(self):
        pass

    @abstractmethod
    def suit_consumption(self):
        pass

    def total_fabric_consumption(self):
        pass


class Clothes(AbstractClothes):

    def __init__(self, coat_size, suit_height):
        self.coat_size = coat_size
        self.suit_height = suit_height

    def coat_consumption(self):
        self.coat_consumption = self.coat_size / 6.5 + 0.5
        return f'Расход ткани на пальто = {self.coat_consumption:.2f}'

    def suit_consumption(self):
        self.suit_consumption = self.suit_height * 2 + 0.3
        return f'Расход ткани на костюм = {self.suit_consumption:.2f}'

    @property
    def total_fabric_consumption(self):
        return f'Общий расход ткани = {self.coat_consumption + self.suit_consumption:.2f}'


clothes = Clothes(56, 160)

print(clothes.coat_consumption())
print(clothes.suit_consumption())
print(clothes.total_fabric_consumption)