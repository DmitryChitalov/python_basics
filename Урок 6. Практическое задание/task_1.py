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

    red_color_running = 7
    yellow_color_running = 2
    green_color_running = 20

    red_color_name = 'красный'
    yellow_color_name = 'желтый'
    green_color_name = 'зеленый'

    def __init__(self, color):
        self.__color = color
        print(f'\nСоздан TrafficLight {self.__color}')

    def switch_light(self, color, wait_time):
        self.wait_time = wait_time
        print(f'Включен {color} свет, ждите {self.wait_time} сек')
        time.sleep(self.wait_time)

    def running(self, color = ''):

        if not color:
            loc_color = self.__color
        else:
            loc_color = color

        if loc_color == self.red_color_name:
            self.switch_light('красный', self.red_color_running)
            self.switch_light('желтый', self.yellow_color_running)
            self.switch_light('зеленый', self.green_color_running)
        elif loc_color == self.yellow_color_name:
            self.switch_light('желтый', self.yellow_color_running)
            self.switch_light('зеленый', self.green_color_running)
        else:
            self.switch_light('зеленый', self.green_color_running)

        print('Цикл переключения цветов завершен')

tl1 = TrafficLight('красный')
tl1.running()

tl2 = TrafficLight('желтый')
tl2.running()

tl3 = TrafficLight('зеленый')
tl3.running()

tl1 = TrafficLight('красный')
tl1.running('желтый')