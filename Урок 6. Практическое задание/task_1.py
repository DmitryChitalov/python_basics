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


def out_red(text):
    print("\033[31m {}".format(text))


def out_yellow(text):
    print("\033[33m {}".format(text))


def out_green(text):
    print("\033[32m {}".format(text))


class TrafficLight:
    __color = ['red', 'green', 'yellow']

    def running (self):
        while True:
            out_red('RED')
            sleep(7)
            out_yellow('YELLOW')
            sleep(2)
            out_green('GREEN')
            sleep(7)
            out_yellow('YELLOW')
            sleep(2)


TrafficLight = TrafficLight()
TrafficLight.running()
