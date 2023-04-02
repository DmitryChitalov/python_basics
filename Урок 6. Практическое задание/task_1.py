"""
Задание 1.

Создать класс TrafficLight (светофор)
и определить у него один приватный атрибут color (цвет) и публичный метод running (запуск).

В рамках метода running реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.
Для имитации "горения" каждого цвета используйте ф-цию sleep модуля time

Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый).

Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""
import time

"""создаю класс определяю приватный атрибут"""


class TrafficLight:
    __color = 3

    """создаю публичный метод"""

    def running(self, red, yellow, green):
        print("\033[31m{}".format("красный"))
        time.sleep(red)
        print("\033[33m{}".format("жёлтый"))
        time.sleep(yellow)
        print("\033[32m{}".format("зеленый"))
        time.sleep(green)


"""создание и вызов метода"""
light_run = TrafficLight()

light_run.running(7, 2, 4)
