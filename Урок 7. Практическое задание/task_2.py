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


class AbsClassClothes(ABC):
    @abstractmethod
    def get_material_rate(self):
        pass


class Clothes(AbsClassClothes):
    name: str
    size: float

    def __init__(self, my_name, my_size):
        self.name = my_name
        self.size = my_size

    @property
    def get_material_rate(self):
        material_rate = 0.0
        if self.name == "Пальто":
            material_rate = self.size / 6.5 + 0.5
        elif self.name == "Костюм":
            material_rate = self.size * 2 + 0.3
        else:
            material_rate = 0

        return material_rate


costume = Clothes("Костюм", 10)
palto = Clothes("Пальто", 10)

print(f"Расход ткани на пальто = {round(palto.get_material_rate, 2)}" )
print(f"Расход ткани на костюм = {round(costume.get_material_rate, 2)}")
print(f"Общий расход ткани = {round(palto.get_material_rate, 2) + round(costume.get_material_rate, 2)}")