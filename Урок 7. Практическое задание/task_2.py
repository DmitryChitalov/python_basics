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
    def __init__(self, value):
        self.value = value

    @abstractmethod
    def my_method_1(self):
        print("Тип одежды:", end=' ')

    @abstractmethod
    def my_method_2(self):
        print("Параметры одежды:", end=' ')

    @abstractmethod
    def my_method_3(self):
        print("Расход ткани:", end=' ')


class Coat (Clothes):
    def my_method_1(self):
        super().my_method_1()
        print("Пальто")

    def my_method_2(self):
        super().my_method_2()
        print("Размер")

    def my_method_3(self):
        super().my_method_3()
        return float(self.value) / 6.5 + 0.5


class Suit (Clothes):
    def my_method_1(self):
        super().my_method_1()
        print("Костюм")

    def my_method_2(self):
        super().my_method_2()
        print("Рост")

    def my_method_3(self):
        super().my_method_3()
        return 2 * float(self.value) + 0.3


class Total:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return (self.a / 6.5 + 0.5) + (2 * self.b + 0.3)


size_coat = 3
size_suit = 4

print("\n")
c = Coat(size_coat)
c.my_method_1()
c.my_method_2()
print("%.2f" % c.my_method_3())


print("\n")
s = Suit(size_suit)
s.my_method_1()
s.my_method_2()
print("%.2f" % s.my_method_3())


t = Total(size_coat, size_suit)
print("\nОбщий расход ткани: %.2f" % t.sum())