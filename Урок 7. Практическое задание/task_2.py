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
class cloth:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_total_topcoat(self):
        return self.width / 6.5 + 0.5

    def get_total_сostume(self):
        return self.height * 2 + 0.3

    @property
    def get_full_total(self):
        return str(f'Общие затраты ткани: {(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}')


class Topcoat(cloth):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.total_topcoat = self.width / 6.5 + 0.5

    def __str__(self):
        return f'Зараты ткани на пальто: {self.total_topcoat}'


class Сostume(cloth):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.total_costume = self.height * 2 + 0.3

    def __str__(self):
        return f'Затраты ткани на костюм: {self.total_costume}'


topcoat = Topcoat(40, 1.4)
costume = Сostume(17, 1.7)
print(topcoat)
print(costume)
print(f'{topcoat.get_full_total} на пальто')
print(f'{costume.get_full_total} на костюм')