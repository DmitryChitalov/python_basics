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
    color = ''

    def change_color(self, color, delay):

        self.color = color
        print(f'{self.color} - {delay}s')
        time.sleep(delay) 

    def running(self, count):
        counter = count
        print('switch on')
        while counter > 0:
            self.change_color('red', 7)
            self.change_color('yellow', 2)
            self.change_color('green', 8)
            self.change_color('yellow', 2)
            counter -= 1
        
        print('switch off')

traffic_light = TrafficLight()
traffic_light.running(2)
