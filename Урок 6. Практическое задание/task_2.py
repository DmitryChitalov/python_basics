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
 
    def __init__(self, length, width ):
        self._length = length
        self._width = width
    
    def mass_calculation(self, mass, thickness):
        sum_mass_road = self._length * self._width * mass * thickness
        print(f'{self._length}м*{self._width}м*{mass}кг*{thickness}м = {sum_mass_road} кг = {int(sum_mass_road / 1000)} т')

road = Road(20, 5000)
road.mass_calculation(25, 0.05)

    
    