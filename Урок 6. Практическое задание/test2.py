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

Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т
"""
from typing import Any


class New_road:
    __length = None
    __width = None
    mass = None
    thin = None
    def __int__(self, length, width):
        self.length = length
        self.widht = width
        print('Road Builded')

    def intake(self):
        self.mass = 25
        self.thin = 0.05
        intake = self.length * self.widht * self.mass * self.thin / 1000
        print(f'print {intake}')


road_to_v = New_road()
road_to_v.intake()

"""
class Road:
    __length = None
    __width = None
    weigth = None
    tickness = None
    def __init__(self, length, width):
        self.length = length
        self.width = width
        print('Create road_to_village object')

    def intake(self):
        self.weigth = 25
        self.tickness = 0.05
        intake = self.length * self.width * self.weigth * self.tickness / 1000
        print(f'Need {intake} ton for the building')

road_to_village = Road(10000, 10)
road_to_village.intake()"""
