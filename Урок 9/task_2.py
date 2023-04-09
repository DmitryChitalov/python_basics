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
    _width = 0
    _length = 0

    def __init__(self, length, width, mass, thickness):
        self._length = float(length)
        self._width = float(width)
        self.mass = float(mass)
        self.thickness = float(thickness)

    def mass_calculation(self):
        result = int(self._length * self._width * self.mass * self.thickness)
        return print(f'Требуемая масса асфальта = {result}(кг) '
                     f'= {int(result / 1000)}(т)')


road_one = Road(input('Введите длинну(м): '), input('Введите ширину(м): '),
                input('Введите массу(кг): '), input('Введите толщину(м): '))
road_one.mass_calculation()