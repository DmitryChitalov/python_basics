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


class Clothes:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def coat(self):
        return self.width / 6.5 + 0.5

    def jacket(self):
        return self.height * 2 + 0.3

    @property
    def all(self):
        return str(f'Общий расход ткани: \n'
                   f' {(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}')


class Coat(Clothes):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.fabric_c = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'Расход ткани на пальто: {self.fabric_c} '


class Jacket(Clothes):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.fabric_j = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Расход ткани на костюм: {self.fabric_j}'

coat = Coat(1, 3)
jacket = Jacket(2, 3)
print(coat)
print(jacket)
print(coat.all)