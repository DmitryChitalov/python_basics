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


class TrafficLight:
    __color = ''

    def __init__(self):
        self.color_and_duration = [('red', 7), ('yellow', 2), ('green', 5)]

    def running(self):
        for color, duration in self.color_and_duration:
            self.__color = color
            print(f'Цвет светофора: {self.__color}, продолжительность: {duration}')
            time.sleep(duration)


trafficlight = TrafficLight()
trafficlight.running()
