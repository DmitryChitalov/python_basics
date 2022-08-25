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

COAT = 1
COSTUME = 2


class ClothesAbs(ABC):
    cloth_type = 0  # COAT, COSTUME
    v = 0
    h = 0

    @abstractmethod
    def get_fabric_consumption(self):
        pass


class Clothes(ClothesAbs):

    def __init__(self, type, param):
        if type == COAT:
            self.cloth_type = COAT
            self.v = param
        elif type == COSTUME:
            self.cloth_type = COSTUME
            self.h = param
        else:
            print("Неверный тип одежды")
            exit(1)

    @property
    def get_fabric_consumption(self):
        if self.cloth_type == COAT:
            return self.v / 6.5 + 0.5
        elif self.cloth_type == COSTUME:
            return 2 * self.h + 0.3
        else:
            print("Неверный тип одежды, подсчет не проведен")
            return 0


cloth_1 = Clothes(COSTUME, 2)
print(f"Расход ткани на костюм составит: {cloth_1.get_fabric_consumption}")

cloth_2 = Clothes(COAT, 4)
print(f"Расход ткани на пальто составит: {cloth_2.get_fabric_consumption}")

print(f"Общий расход ткани: {cloth_1.get_fabric_consumption + cloth_2.get_fabric_consumption}")
