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
from itertools import cycle


class TrafficLight:
    """ Определение переменных"""
    __modes = (('red', 7), ('yellow', 2), ('green', 5))
    __light_start = 0
    __next_light = 0

    def __init__(self):
        self.__color = self.__modes[0][0]
        self.__tic()

    def running(self):
        """Основной цикл проверяет поменялся-ли цвет, и выводит его на экран."""
        prew_color = None
        while True:
            self.__tic()
            if prew_color != self.__color:
                prew_color = self.__color
                print(self.__color)

    def __tic(self):
        """В зависимости от прошедшего времени переключаем цвет светофора."""
        if self.__light_start + dict(self.__modes)[self.__color] <= time.time():
            self.__color, self.__light_start = self.__modes[self.__next_light][0], time.time()
            self.__next_light = self.__next_light + 1 if len(self.__modes) > self.__next_light + 1 else 0

    def color(self):
        self.__tic()
        return self.__color


if __name__ == '__main__':
    light = TrafficLight()
    time.sleep(0.5)
    light2 = TrafficLight()
    time.sleep(0.5)
    light3 = TrafficLight()
    time.sleep(0.5)
    for light in cycle((light, light2, light3)):
        print(light.color())
        time.sleep(1)
