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
    weight_per_m = 25
    as_thickness = 0.05

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc(self):
        res1 = (self._length * self._width * Road.weight_per_m * Road.as_thickness)
        res2 = res1 * 0.001
        print(f'Требуется масса в {res1} кг ({res2} тонн) асфальта на покрытие дорож. полотна')


m4_don = Road(5000, 20)
m11_spb = Road(11000, 30)
m4_don.calc()
m11_spb.calc()