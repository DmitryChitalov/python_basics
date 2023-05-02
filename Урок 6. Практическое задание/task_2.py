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

    thickness = 0.05
    weight = 25

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def asphalt_weight(self, length, width):
        if not length:
            length = self.__length
        if not width:
            width = self.__width
        asphalt_weight = int(length) * int(width) * self.weight * self.thickness
        print(f'\nМасса асфальта для покрытия дорожного полотна длиной {length} метров и шириной {width} метров ' 
              f'равна {asphalt_weight} кг = {asphalt_weight//1000} т')


example_road = Road('5000', '20')
example_road.asphalt_weight('', '')
example_road.asphalt_weight(10000, 50)
