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
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_asphalt_mass(self, asphalt_weight, thickness):
        return self.length * self.width * thickness * asphalt_weight


road = Road(5000, 20)
asphalt_weight = 25
thickness = 0.05

asphalt_mass = road.calculate_asphalt_mass(asphalt_weight, thickness)
print(f"Масса асфальта для покрытия дороги: {asphalt_mass:.0f} кг или {asphalt_mass / 1000:.0f} т")
