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
    asphalt_weight = 25
    asphalt_thickness = 0.05

    def __init__(self, asphalt_length, asphalt_width):
        self._length = asphalt_length
        self._width = asphalt_width

    def calc(self):
        asphalt_mass = int((self._length * self._width * Road.asphalt_weight * Road.asphalt_thickness))
        asphalt_massT = int(asphalt_mass / 1000)
        print(f"Требуется {asphalt_mass} кг = {asphalt_massT} тонн")


road_lw = Road(20, 5000)
road_lw.calc()