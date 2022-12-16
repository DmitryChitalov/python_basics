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
    def __init__(self, color):
        self._color = color

    def running(self):
        if self._color == 'красный':
            print(self._color)
            time.sleep(7)
        elif self._color == 'желтый':
            print(self._color)
            time.sleep(2)
        else:
            print(self._color)
            time.sleep(7)


tl1 = TrafficLight('красный')
tl1.running()
tl1 = TrafficLight('желтый')
tl1.running()
tl1 = TrafficLight('зелёный')
tl1.running()