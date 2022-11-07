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
from datetime import datetime


class TrafficLight:
    """"
    Class TrafficLight
    """
    __COLOR_STOP__ = "red"
    __COLOR_WAIT__ = "yellow"
    __COLOR_RUN__ = "green"

    __color = __COLOR_STOP__

    def running(self, iterations):
        """
        :param iterations:
        :return:
        """

        while iterations > 0:
            print(f"traffic color is: {self.__color} ("
                  f"{datetime.now().strftime('%H:%M:%S')})")

            if self.__color == self.__COLOR_STOP__:
                time.sleep(7.0)
                self.__color = self.__COLOR_WAIT__
                continue
            if self.__color == self.__COLOR_WAIT__:
                time.sleep(2.0)
                self.__color = self.__COLOR_RUN__
                continue
            if self.__color == self.__COLOR_RUN__:
                time.sleep(5.0)
                self.__color = self.__COLOR_STOP__
                iterations -= 1


traffic = TrafficLight()
traffic.running(3)
