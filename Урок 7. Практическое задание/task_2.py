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
    def obj_type(self):
        print("\nТип:", end=" ")

    @abstractmethod
    def obj_param(self):
        print("Параметр:", end=" ")
        pass

    @abstractmethod
    def obj_consumption(self):
        print("Расход:", end=" ")
        pass


class Coat(Clothes):
    @property
    def obj_type(self):
        super().obj_type()
        print("Пальто")

    @property
    def obj_param(self):
        super().obj_param()
        print(f"Размер {size_coat}")

    @property
    def obj_consumption(self):
        super().obj_consumption()
        return float(self.value) / 6.5 + 0.5


class Suit(Clothes):
    @property
    def obj_type(self):
        super().obj_type()
        print("Костюм")

    @property
    def obj_param(self):
        super().obj_param()
        print(f"Рост {height_suit}")

    @property
    def obj_consumption(self):
        super().obj_consumption()
        return 2 * float(self.value) + 0.3


class Total:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return (self.a / 6.5 + 0.5) + (2 * self.b + 0.3)


size_coat = int(input("Введите размер пальто: "))
height_suit = int(input("Введите рост костюма: "))

# print("\n")
c = Coat(size_coat)
c.obj_type
c.obj_param
print(f"{round(c.obj_consumption, 2)}")


# print("\n")
s = Suit(height_suit)
s.obj_type
s.obj_param
print(s.obj_consumption)

t = Total(size_coat, height_suit)
print(f"\nОбщий расход материала: {round(t.sum(), 2)}")


input("\nНажмите Enter...")
