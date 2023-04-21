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
    def __init__(self, length, width, mass_road, thickness):
        self.__length = length
        self.__width = width
        self.mass_road = mass_road
        self.thickness = thickness

    def sum_road(self):
        res = self.__length * self.__width * self.mass_road * self.thickness
        print(f'{self.__length}м*{self.__width}м*{self.mass_road}кг*{self.thickness}м = {res} кг = {res // 1000} т')


user_length = int(input('Укажите длину асфальта (в метрах): '))
user_width = int(input('Укажите ширину асфальта (в метрах): '))
user_mass = int(input('Укажите массу асфальта (в кг): '))
user_thickness = float(input('Укажите толщину полотна (в метрах): '))

r = Road(user_length, user_width, user_mass, user_thickness)
r.sum_road()