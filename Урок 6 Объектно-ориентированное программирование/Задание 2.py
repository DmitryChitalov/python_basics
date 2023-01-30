"""Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу:
длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна.
Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
"""
import re

# 20м 5000м 25кг 5см
string = ''
while len(string) < 4:
    inp = input('Enter length, width, mass, thickness with space: ')
    st = re.split('[a-zA-Zа-яА-Я]', inp)
    string = ''.join(st).split()
# чтобы код был понятен для другого человека
length = int(string[0])
width = int(string[1])
mass = int(string[2])
thickness = int(string[3])


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def formula(self, mass, thickness):
        s = self._length * self._width
        m = (self._length * self._width * mass * thickness) // 1000
        s1 = m / s
        return f'{m} tons of asphalt need ({s1} tons or {int(s1 * 1000)} kg of asphalt need for 1 m^2 of road)'


x = Road(length, width)
am = x.formula(mass, thickness)
print(am)

"""
Enter length, width, mass, thickness with space: 20 5000 25 5
12500 tons of asphalt need (0.125 tons or 125 kg of asphalt need for 1 m^2 of road)
"""
