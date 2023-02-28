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
# from time import sleep


# class Trafficlight:

#     __color__ = cycle

#     def running(self):
#         if self.__color__ == 'Красный':
#             print("Загорелся красный свет")
#         sleep(7)
#         print("Загорелся желтый свет")
#         sleep(2)
#         print("Загорелся зеленый свет")
#         sleep(3)


# obj = Trafficlight('Красный')
# obj.color()

from itertools import cycle
from time import sleep


class TrafficLight:
    __color__ = cycle([
        ['Красный', 7],
        ['Желтый', 2],
        ['Зеленый', 5],
        ['Желтый', 2]
    ])

    def running(self):
        light = next(self.__color__)
        print(f'Горит {light[0]} свет, осталось {light[1]} секунд')
        sleep(light[1])


traffic_light = TrafficLight()
traffic_light.running()
traffic_light.running()
traffic_light.running()
traffic_light.running()
