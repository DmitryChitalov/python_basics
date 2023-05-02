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
    color = None

    def __init__(self, r_time: int, y_time: int, g_time: int):
        self.r_time = r_time
        self.y_time = y_time
        self.g_time = g_time

    def running(self):
        while True:
            i = 1
            while i <= (self.r_time + self.y_time + self.g_time):
                if i in range(1, self.r_time + 1):
                    self.color = ("Red")
                    print(f"{i} {self.color}")
                elif i in range(self.r_time, self.r_time + self.y_time + 1):
                    self.color = ("Yellow")
                    print(f"{i} {self.color}")
                elif i in range(self.r_time + self.y_time, self.r_time + self.y_time + self.g_time + 1):
                    self.color = ("Green")
                    print(f"{i} {self.color}")
                time.sleep(1)
                i += 1


light = TrafficLight(7, 2, 10)
light.running()
