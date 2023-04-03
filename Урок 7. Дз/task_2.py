"""
Задание 2.
Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
__length (длина в метрах), width (ширина в метрах).

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
    def __init__(self, length, width, weight, thickness):
        self._length = length
        self._width = width     # Protected
        self.weight = weight    # Public
        self.thickness = thickness
        self.result = length * width * self.weight * self.thickness

    def weight_total(self):
        return self.result / 1000


omsk_new = Road(20, 5000, 25, 0.05)
print(f"Масса полотна: {omsk_new.weight_total()} тонн")
