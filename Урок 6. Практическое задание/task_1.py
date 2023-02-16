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
from os import system
# color = ["RED", "YELLOV", "GREEN"]
# color = ["RED", "YELLOV", "GREEN"]
# for i in my_time:
#     for el in color:
#         print(el)
#         sleep(i)


class TrafficLight:
    _color = {7: "RED", 2: "YELLOV", 5: "GREEN", 2.01: "YELLOV"}

    def runing(self):
        print(' ' * 6, end='\r')
        for key, value in self._color.items():
            print(value, end='\r')
            sleep(key)
            print(' ' * 10, end='\r')


traflite = TrafficLight()
s = 0
while s < 10:
    traflite.runing()
s += 1
