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
from time import sleep
from itertools import cycle


class TrafficLight:
    def __init__(self):
        self.__color = {"red": 7, "yellow": 2, "green": 5}


    def running(self):
        print("Для остановки светофора нажмите Ctrl+C")
        for color, delay in cycle(self.__color.items()):
            print(color)
            sleep(delay)
            

traffic_light = TrafficLight()
traffic_light.running()
