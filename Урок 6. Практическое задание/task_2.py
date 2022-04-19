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
import time
import threading


class TrafficLight:
    def __init__(self, _colors2, _colors):
        pass

    _color = None
    _colors2 = ['red']
    _colors = ['yellow', 'green']

def running():
    c = 0
    while c < 1:
        for element in TrafficLight._colors2:
            print(element)
            c += 1
            time.sleep(7)


def running2():
    c = 0
    while c < 1:
        for element in TrafficLight._colors:
            print(element)
            c += 1
            time.sleep(2)


t1 = threading.Thread(target=running())
t2 = threading.Thread(target=running2())

t1.start()
t2.start()
