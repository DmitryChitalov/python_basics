from abc import ABC, abstractmethod


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


class MyAbstractClothes (ABC):
    @abstractmethod
    def get_coat_consumption(self):
        pass

    @abstractmethod
    def get_suit_consumption(self):
        pass

    @abstractmethod
    def get_total_consumption(self):
        pass


class Clothes (MyAbstractClothes):
    def __init__(self, v, h):
        self.v = v
        self.h = h

    def get_coat_consumption(self):
        try:
            print(f"Расход ткани на пальто = {round((self.v / 6.5 + 0.5), 2)}")
        except BaseException as e:
            print(f"General error: {e}")

    def get_suit_consumption(self):
        try:
            print(f"Расход ткани на костюм = {round((2 * self.h + 0.3), 2)}")
        except BaseException as e:
            print(f"General error: {e}")

    @property
    def get_total_consumption(self):
        try:
            return f"Общий расход ткани = {round(self.v / 6.5 + 0.5 + (2 * self.h + 0.3), 2)}"
        except BaseException as e:
            print(f"General error: {e}")


my_clothes = Clothes(5, 7)
my_clothes.get_coat_consumption()
my_clothes.get_suit_consumption()
print(my_clothes.get_total_consumption)
