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
    traffic = {"red": 7, "yellow": 2, "green": 5}
    __color = "red"

    def __init__(self, color="red"):
        self.__color = color

    def running(self, var_cicle):
        for i in range(var_cicle):
            print(self.__color)
            time.sleep(self.traffic[self.__color])
            if self.__color == "red":
                self.__color = "yellow"
            elif self.__color == "yellow":
                self.__color = "green"
            else:
                self.__color = "red"


obj = TrafficLight()
obj.running(5)
