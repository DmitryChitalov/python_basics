"""
Задание 1.
Создать класс TrafficLight (светофор) и определить у него один приватный атрибут color (цвет) и публичный метод running (запуск).

В рамках метода running реализовать переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. 
Для имитации "горения" каждого цвета испольщуйте ф-цию sleep модуля time

Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый).

Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""
import time


class TrafficLight:

    def __init__(self):
        self.__color = 'Red'

    def running(self):
        while True:
            if self.__color == 'Red':
                print('Red')
                time.sleep(7)
                self.__color = 'Yellow'
            elif self.__color == 'Yellow':
                print('Yellow')
                time.sleep(2)
                self.__color = 'Green'
            else:
                print('Green')
                time.sleep(15)
                self.__color = 'Red'


light = TrafficLight()
light.running()
