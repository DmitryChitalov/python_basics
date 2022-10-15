"""
Задание 2.

Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
length (длина в метрах), width (ширина в метрах).

Значения данных атрибутов должны передаваться при создании экземпляра класса.

Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
всего дорожного полотна.

Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
Массу и толщину сделать публичными атрибутами.
Проверить работу метода.

Например: 20м*5000м*25кг*0.05м = 12500000кг = 12500 т
"""
from os import system, name as osname


def cls():
    system('cls' if osname == 'nt' else 'clear')


class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.mass = 25
        """
        примерный расход асфальта на 1 кв.м.
        при толщине слоя 1 см равен 25 кг
        """
        self.thickness = 5

    def calculate_mass_asfalt(self):
        mass = self._width * self._length * self.mass * self.thickness
        print(f"Для ремонта дорожного полотна толщиной в {self.thickness} см")
        print(f"Длинной {self._length}м и шириной {self._width}м")
        print(f"потребуется {mass/1000} тонн асфальта.\n")


cls()
rd = Road(5000, 20)
rd.calculate_mass_asfalt()
