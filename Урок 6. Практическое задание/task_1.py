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


class Traffic_light:
    def __init__(self, color):
        self.__color = color

    def running(self):
        def time_color(count):
            while count != 1:
                sleep(1)
                count -= 1
                print(f'color = {self.__color}. time = {count}')

        if self.__color == 'red':
            count_time = 8
            time_color(count_time)
            self.__color = 'yellow'

        if self.__color == 'yellow':
            count_time = 3
            time_color(count_time)
            self.__color = 'green'

        if self.__color == 'green':
            count_time = 15
            time_color(count_time)
            self.__color = 'red'


run = Traffic_light('red')
run.running()
