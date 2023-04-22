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

class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']
    __time_shift = [7, 2, 7]

    def running(self):
        i = 0
        while i != 3:
            print(TrafficLight.__color[i])
            for k in range(TrafficLight.__time_shift[i]):
                sleep(1)
                print(k + 1)
            i += 1



my_traffic_light = TrafficLight()
my_traffic_light.running()


