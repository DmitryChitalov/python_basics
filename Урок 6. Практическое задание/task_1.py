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

class TrafficLight():
    red_time = 7
    yellow_time = 2
    green_time = 4

    def __init__(self, color):
        self.__color = color

    def switch_color(self, color, color_time):
        self.color_time = color_time
        print(f'{color} свет. Следующий через {color_time} сек.')
        time.sleep(self.color_time)

    def running(self):
        self.switch_color('красный', self.red_time)
        self.switch_color('желтый', self.yellow_time)
        self.switch_color('зеленый', self.green_time)

a = TrafficLight('красный')
a.running()
