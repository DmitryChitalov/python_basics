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


from itertools import cycle
from time import sleep


class TrafficLight:
    """A dummy docstring."""
    c = cycle([
        {'s': 'красный', 'd': 7},
        {'s': 'желтый', 'd': 2},
        {'s': 'зеленый', 'd': 10},
    ])

    def running(self):
        """A dummy docstring."""
        light = next(self.c)
        print(f"{light['s']} - {light['d']} сек.")
        sleep(light['d'])


traffic_light = TrafficLight()
traffic_light.running()
traffic_light.running()
traffic_light.running()
traffic_light.running()
