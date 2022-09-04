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

    def __init__(self, _length, _width, weight, thickness):
        self._length = _length
        self._width = _width
        self.weight = weight
        self.thickness = thickness

    def road_mass(self):
        road_len = self._length
        road_wid = self._width
        road_wei = self.weight
        road_thick = self.thickness
        overall = road_len * road_wid * road_wei * road_thick // 100
        return print(f"\nМасса асфальта - {road_len}м * {road_wid}м * {road_wei}кг * {road_thick}см =", overall, "кг",
                     "=", overall // 1000, "т")


call = Road(20, 5000, 25, 5)
call.road_mass()
