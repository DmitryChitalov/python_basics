"""
Задание 1.

Создать класс TrafficLight (светофор)
и определить у него один приватный атрибут color (цвет) и публичный метод running (запуск).

В рамках метода running реализовать переключение светофора в режимы:
окрасный, желтый, зеленый. Продлжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.
Для имитации "горения" каждого цвета испольщуйте ф-цию sleep модуля time

Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый).

Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""
from time import sleep


def time_color(time_light, color):
    while time_light != 1:
        time_light -= 1
        sleep(1)
        print(f'Цвет светофора - {color}. Осталось времени {time_light} sec')


class TrafficLight:
    def __init__(self, color):
        self.__color = color

    def running(self):
        for i in range(3):
            if self.__color == 'зеленый':
                count = 10
                time_color(count, self.__color)
                self.__color = 'красный'

            elif self.__color == 'желтый':
                count = 3
                time_color(count, self.__color)
                self.__color = 'зеленый'

            elif self.__color == 'красный':
                count = 8
                time_color(count, self.__color)
                self.__color = 'желтый'


tr = TrafficLight('зеленый')
tr.running()
