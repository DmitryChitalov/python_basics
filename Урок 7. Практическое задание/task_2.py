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

# Подключаем модули
from abc import ABC, abstractmethod

# Выводим на экран задание
print('\nУрок 7 Задание 1\n')

# Объявляем классы и методы
class AbstractClothers(ABC):
    @abstractmethod
    def coat_exp(self):
        pass

    @abstractmethod
    def suit_exp(self):
        pass


class Cloth(AbstractClothers):
    def __init__(self, v, h):
        self.v = v
        self.h = h

    @property
    def coat_exp(self):
        coat_expend = self.v / 6.5 + 0.5
        return coat_expend

    @property
    def suit_exp(self):
        suit_expend = self.h * 2 + 0.3
        return suit_expend

    @property
    def summ_exp(self):
        summ_expend = self.coat_exp + self.suit_exp
        return summ_expend

    def __str__(self):
        print(f'Всего потребуется {self.summ_exp:.2f} едениц ткани')
        return ''

# Объявляем переменные и выводим результат методов на экран
size = float(input('Введите размер пальто: '))
height = float(input('Введите рост для изготовления костюма: '))
clothes = Cloth(size, height)
print(f'Для изготовления {clothes.v} размера пальто потребуется {clothes.coat_exp:.2f} едениц ткани.\n')
print(f'Для изготовления костюма на рост {clothes.h} потребуется {clothes.suit_exp:.2f} едениц ткани.\n')
# Общий расход
print(clothes)
