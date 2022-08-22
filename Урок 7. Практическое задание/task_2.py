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


class AbcClothes(ABC):
    type_сlothes = ["пальто", "костюм"]
    __cloth_add = 0
    __cloth_ratio = 0

    def __init__(self, ind_type):
        self.ind_type = ind_type

    @abstractmethod
    def cloth(self):
        return 0


class Clothes(AbcClothes):

    def __init__(self, ind_type, parametr):
        super().__init__(ind_type)
        if super().type_сlothes[ind_type] == "пальто":
            self._v = parametr
            self.__cloth_add = 0.5
            self.__cloth_ratio = 6.5
        elif super().type_сlothes[ind_type] == "костюм":
            self._h = parametr
            self.__cloth_add = 0.3
            self.__cloth_ratio = 2

    def cloth(self):
        if super().type_сlothes[self.ind_type] == "пальто":
            return self._v / self.__cloth_ratio + self.__cloth_add
        elif super().type_сlothes[self.ind_type] == "костюм":
            return self.__cloth_ratio * self._h + self.__cloth_add

    @property
    def parametr_cloth(self):
        if super().type_сlothes[self.ind_type] == "пальто":
            return f"Пальто V = {self._v}"
        elif super().type_сlothes[self.ind_type] == "костюм":
            return f"Костюм H = {self._h}"

    @parametr_cloth.setter
    def parametr_cloth(self, v_value):
        if super().type_сlothes[self.ind_type] == "пальто":
            self._v = v_value
        elif super().type_сlothes[self.ind_type] == "костюм":
            self._h = v_value


product_1 = Clothes(0, 5)
product_2 = Clothes(1, 5)
print(product_1.cloth())
print(product_2.cloth())
print(product_1.parametr_cloth)
product_1.parametr_cloth = 50
print(product_1.parametr_cloth)
print(product_2.parametr_cloth)
product_2.parametr_cloth = 15
print(product_2.parametr_cloth)
print(product_1.cloth())
print(product_2.cloth())
lst = [product_1, product_2, product_2]
lst_count = [0, 0]
for i in lst:
    lst_count[i.ind_type] += i.cloth()

print(f"Общий расход ткани {sum(lst_count)}")
for idx, i in enumerate(lst_count):
    print(f"Расход на {Clothes.type_сlothes[idx]} = {i}")
