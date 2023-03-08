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
from datetime import datetime as dt

class TrafficLight:
    _states = {'red': 7, 'yellow': 2, 'green': 9}
    _color = ''

    def running(self):
        for color, sw_time in self._states.items():
            self._color = color
            start_state_time = dt.now()

            print(f"TrafficLight switched to state '{self._color}' "
                  f"on {sw_time} seconds")

            sleep(sw_time)

            print(f"TrafficLight leave state '{self._color}' after" 
                  f"{(dt.now() - start_state_time).seconds} seconds")


if __name__ == '__main__':
    tl = TrafficLight()
    tl.running()
