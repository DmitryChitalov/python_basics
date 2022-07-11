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
    def consumption(self):
        pass


class Clothes:

    def __init__(self, t):
        self.t = t

    @property
    def coat(self):
        return round(self.t.get('coat') / 6.5 + 0.5, 2)

    @property
    def costume(self):
        return round(2 * self.t.get('costume') + 0.3, 2)

    def total(self):
        return self.coat + self.costume

    def consumption(self):
        print(f"Расход ткани на пальто = {self.coat}")
        print(f"Расход ткани на костюм = {self.costume}")
        print(f"Общий расход ткани = {self.total()}")


c = Clothes(dict(coat=52, costume=176))
c.consumption()
