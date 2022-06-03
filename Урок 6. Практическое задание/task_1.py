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

colors = ["Red", "Yellow", "Green"]


class TrafficLight:
    __color: str = ""

    def running(self):
        for i in range(0, 10):
            index = i % 3
            self.__color = colors[index]
            print(f'The traffic light switches to: {self.__color}')
            if index == 0:
                sleep(7)
            elif index == 1:
                sleep(2)
            else:
                sleep(10)


traffic_light = TrafficLight()
traffic_light.running()
