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
# from time import sleep
# from itertools import cycle

# class TrafficLight:
#     def __init__(self):
#         self.__color = (('red', 5), ('yellow', 2), ('green', 5))

#     def running(self):
#         '''работа светофора'''
#         for color, sec in cycle(self.__color):
#             print(color, '(wait {} sec)'.format(sec))
#             sleep(sec)

# traffic_light = TrafficLight()
# traffic_light.running()

# # for i in range(7, -1, -1):
# #     time.sleep(1)
# #     print(f'\r{i}', end='')

from time import sleep

class TrafficLight:
    def __init__(self):
        self.__color = "red", "yellow", "green"
        self.__delay = [[0, 1, 0, 0], [0, 7, 2, 3]]
    
    def running(self, x):
        for color in self.__color:
            for i in self.__delay[x]:
                print(f"{color} waiting {i} sec")
                print(i)
                sleep(i)

traffic_light = TrafficLight()
user_input = int(input("Выберите, пожалуйста, режим работы светофора. 1 для обычного и 0 для тестирования: "))
traffic_light.running(user_input)

# while 0 < user_input < 2:
#     user_input = int(input("Выберите, пожалуйста, режим работы светофора. 1 для обычного и 0 для тестирования: "))
# else:
#     traffic_light.running(user_input)

# if user_input == 1:
#     traffic_light.running()
# else:
#     traffic_light.running()
