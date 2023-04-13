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
    weight = 0
    thickness = 0

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def res(self):
        self.weight = 25
        self.thickness = 0.5
        res = self.__length * self.__width * self.weight * self.thickness
        print(f'Required asphalt mass is calculated for the road - {res} 
')


Road = Road(20, 5000)
Road.res()

