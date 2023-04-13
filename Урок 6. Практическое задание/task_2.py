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
    mass = 1
    thickness = 1.0
    _length = 0
    _width = 0

    def __init__(self, length, width):
        self._width = width
        self._length = length

    def calc(self):
        return self._length * self._width * self.mass * self.thickness


rd = Road(20, 5000)
rd.mass = 25
rd.thickness = 0.05
print(rd.calc())
