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


class TrafficLight:
    __color = 'red'

    def __init__(self):
        pass

    def running(self):
        while True:
            wait = 4
            next_color = self.__color
            if self.__color == 'red':
                wait = 7
                next_color = 'yellow'
            if self.__color == 'yellow':
                wait = 2
                next_color = 'green'
            if self.__color == 'green':
                wait = 4
                next_color = 'red'

            print(self.__color)
            sleep(wait)
            self.__color = next_color


tl = TrafficLight()
tl.running()
