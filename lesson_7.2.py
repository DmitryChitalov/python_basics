"""
2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""


class Textile:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_total_coat(self):
        return self.width / 6.5 + 0.5

    def get_total_jacket(self):
        return self.height * 2 + 0.3

    @property
    def get_full_total(self):
        return str(f'Общий расход ткани: \n'
                   f' {(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}')


class Coat(Textile):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.total_coat = self.width / 6.5 + 0.5

    def __str__(self):
        return f'Расход на пальто: {self.total_coat}'


class Jacket(Textile):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.total_jacket = self.height * 2 + 0.3

    def __str__(self):
        return f'Расход на костюм: {self.total_jacket}'


coat = Coat(38, 1.6)
jacket = Jacket(35, 1.8)
print(coat)
print(jacket)
print(coat.get_full_total)
print(jacket.get_full_total)
print(jacket.get_total_coat())
print(jacket.get_total_jacket())
