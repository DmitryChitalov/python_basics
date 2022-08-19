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
    _length = 0
    _width = 0

    def __init__(self, road_length, road_width):
        self._length = road_length
        self._width = road_width

    def get_mass(self, asphalt_masse_one_qm, asphalt_thickness):
        return self._length * self._width * asphalt_masse_one_qm * asphalt_thickness


r_length = 20
r_width = 5000
as_masse_one_qm = 25
as_thickness = 0.05

road1 = Road(r_length, r_width)
mass = road1.get_mass(as_masse_one_qm, as_thickness)
print(
    f"Для дороги длиной {r_length} м, шириной {r_width} м, при условии что вес 1 кв асфальта равен {as_masse_one_qm} кг"
    f" и толщиной {as_thickness} м. Понадобиться {mass} кг или {mass / 1000} т")
