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
    _lenght = None
    _width = None
    cover_thickness = None
    cover_weight = None

    def __init__(self, length, width):
        self._length = length
        self._width = width
        
    def cover_amount(self):
        cover_mass = (self._length * self._width *
            self.cover_thickness * self.cover_weight) / 1000
        print(f'Вес дорожного покрытия составит {cover_mass} тонн.')
        
new_road = Road(20, 5000)
new_road.cover_thickness = 0.05
new_road.cover_weight = 25
new_road.cover_amount()
