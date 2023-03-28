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
    # ширина (метр)
    weight = 25
    # толщины полотна (метр)
    thickness = 0.05

    # создание атрибута length и width для класса Road
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calc(self):
        # расчет массы асфальта (тонны), необходимого для покрытия всего дорожного полотна.
        res = (self.length * self.width * Road.weight * Road.thickness) / 1000
        print(f'Необходимо {res} тонн асфальта: ')


res_road = Road(20, 5000)
res_road.calc()