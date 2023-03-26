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
    weight = 25
    depth = 0.05

    def __init__(self, lenght, width):
        self._width = width
        self._length = lenght

    def asphalt_mass(self):
        mass = self.weight * self.depth * self._width * self._length
        return f'Необходимая масса асфальта для производства работ = {mass/1000:.2f} тонн'


road_l_w = Road(5000, 20)
print(road_l_w.asphalt_mass())
