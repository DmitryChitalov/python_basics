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
    __length = 0
    __width = 0

    def __init__(self, length, width):
        """
        :param length: number
        :param width: number
        """
        if length <= 0 or width <= 0:
            raise ValueError("длина и ширина должны быть положительными числами", length, width)
        self.__length = length
        self.__width = width

    def calc_mass(self, density, thickness):
        """
        Mass calculation as w*l*h*rho
        :param density: number
        :param thickness: number
        :return: number, kg
        """
        if density <= 0 or thickness <= 0:
            raise ValueError("плотность и толщина должны быть положительными числами", density, thickness)
        return self.__width * self.__length * density * thickness


if __name__ == '__main__':
    road = Road(500, 10)
    print(f'общая масса асфальта {road.calc_mass(9.35, 5.5) // 1000} тонн')
