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


class Road:
    unit_mass = 25
    thickness = 0.05

    def __init__(self, length, width):
        self._lenght = length
        self._width = width

    def calculation_mass_asphalt(self):
        return self._lenght * self._width * self.unit_mass * self.thickness


road_1 = Road(5000, 20)
road_2 = Road(3500, 10)

Road.unit_mass = 75
print(road_1.calculation_mass_asphalt())
print(road_2.calculation_mass_asphalt())
