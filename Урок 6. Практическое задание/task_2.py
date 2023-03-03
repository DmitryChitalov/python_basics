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

# pylint: disable=missing-class-docstring, missing-function-docstring


class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weight = 25
        self.height = 0.05

    def asphalt_weight(self):
        asphalt_weight = self._length * self._width * self.weight * self.height
        print(f'{self._width}м*{self._length}м*{self.weight}кг*{self.height}м = '
              f'{int(asphalt_weight)} кг = {int((asphalt_weight) / 1000)} т')


road_weight = Road(5000, 20)
road_weight.asphalt_weight()
