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
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def cloths(self):
        pass


class Coat(Clothes):
    def __init__(self, name: str, size: int):
        self.size = size
        super().__init__(name)

    @property
    def cloths(self):
        return round(self.size / 6.5 + 0.5, 2)


class Suit(Clothes):
    def __init__(self, name: str, height: int):
        self.height = height
        super().__init__(name)

    @property
    def cloths(self):
        return round(2 * self.height + 0.3, 2)


class Summ:
    def __init__(self, num_a: int, num_b: int):
        self.a = num_a
        self.b = num_b

    @property
    def cloths(self):
        return self.a / 6.5 + 0.5 + 2 * self.b + 0.3


if __name__ == "__main__":
    c = Coat("пальто", 20)
    s = Suit("костюм", 10)
    print("Расход ткани на пальто =", c.cloths)
    print("Расход ткани на костюм =", s.cloths)
    t = Summ(c.cloths, s.cloths)
    print("\nОбщий расход ткани: %.2f" % t.cloths)