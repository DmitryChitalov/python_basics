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
class Road():
    def __init__(self, _lenght, _width, volume):
        self._lenght = _lenght
        self._width = _width
        self.volume = volume
    def mass(self):
        return self._lenght * self._width

class MassCount(Road):
     def a(self):
         self.volume = volume

r = MassCount(25, 10000, 125)
print(r.mass())

class Mass():
    def __init__(self, _len, _wid, _vol):
        self._len = _len
        self._wid = _wid
        self._vol = _vol
    def m_count(self,_len, _wid, _vol):
        return _len * _wid * _vol
a = Mass(1, 1, 1)
print(a.m_count(2, 1, 2))