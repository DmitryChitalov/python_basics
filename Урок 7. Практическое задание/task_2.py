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

    def get_square_coat(self):
        return self.width / 6.5 + 0.5

    def get_square_suit(self):
        return self.height * 2 + 0.3

    @property
    def get_sq_full(self):
        return str(f'Общий расход ткани = '
                   f' {(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3):.2f}')


class Coat(Clothes):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_coat = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'Расход ткани на пальто = {self.square_coat}'


class Suit(Clothes):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_suit = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Расход ткани на костюм = {self.square_suit}'

coat = Coat(2, 4)
suit = Suit(1, 2)
print(coat)
print(suit)
print(coat.get_sq_full)
print(suit.get_sq_full)
print(suit.get_square_coat())
print(suit.get_square_suit())
