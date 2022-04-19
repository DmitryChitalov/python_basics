"""
Задание 1.

Создать класс TrafficLight (светофор)
и определить у него один приватный атрибут color (цвет) и публичный метод running (запуск).

В рамках метода running реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.
Для имитации "горения" каждого цвета испольщуйте ф-цию sleep модуля time

Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый).

Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""
import time
import threading


class TrafficLight:
    def __init__(self, _colors2, _colors):
        pass

    _color = None
    _colors2 = ['Red - delay 7 sec']
    _colors = ['Yellow - delay 2 sec', 'Green - delay 2 sec']


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
