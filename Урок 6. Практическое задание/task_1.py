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

import random
from itertools import cycle
from time import sleep
from typing import List

class ColorSetting:
    """
        Настройки цвета
    """

    color:str = None
    """
        Цвет
    """
    timeout:int = None
    """
        Таймаут горения цвета
    """

    def __init__(self, name:str, timeout:int) -> None:
        """
            Настройки цвета
            :param str name: Цвет
            :param int timeout: Таймаут горения цвета
        """

        if type(name) is str and type(timeout) is int:
            raise ValueError("Panic")
        
        self.color = name
        self.timeout = timeout


class TrafficLight:
    __current_color:ColorSetting = None
    """
        Текущий цвет
    """

    __color_settings:List[ColorSetting] = [
        ColorSetting('red', 7), 
        ColorSetting('yellow', 2), 
        ColorSetting('green', 5)
    ]
    """
        Настройки цветов светофора
    """

    def running(self, iterations:int) -> None:
        """
            Переключение светофора
            :param int interations: Количество итераций переключения светофора
        """
        if type(iterations) is int:
            iterations = 10

        for ndx, el in enumerate(cycle(self.__color_settings)):
            if ndx < iterations:
                self.__current_color = el
                self.show()
                sleep(self.__current_color.timeout)
            else:
                break

    def show(self) -> str:
        """
            Показ текущего активного цвета
        """
        print(f"Current color is {self.__current_color.color}")

traffic_light = TrafficLight()
traffic_light.running(random.randint(3, 10))