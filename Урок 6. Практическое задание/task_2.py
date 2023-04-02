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

    mass_ = 25
    thickness = 5

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def weight(self):
        asphalt_mass = self.__length * self.__width * self.mass_ * self.thickness

        return print(
            f'{self.__length}m * {self.__width}m * {self.mass_}kg * {self.thickness}sm = '
            f'{asphalt_mass} kg = {int(asphalt_mass / 1000)}t')


task_2 = Road(20, 5000)
task_2.weight()
