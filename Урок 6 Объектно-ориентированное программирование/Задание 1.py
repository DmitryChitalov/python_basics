"""Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный,
желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение.  Переключение между режимами должно осуществляться только в указанном порядке
 (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и
завершать скрипт.
"""

import time
from termcolor import colored

lights = ['red', 'yellow', 'green', 'yellow']


class TrafficLight:
    def __init__(self, color):
        self.__color = color

    def colortraffic(self):
        c1 = "   .....\n .........\n...........\n .........\n  ......."
        cc = "   @@@@@\n @@@@@@@@@\n@@@@@@@@@@@\n @@@@@@@@@\n  @@@@@@@"
        if self.__color == 'red':
            print(colored(cc, self.__color))
            print(c1)
            print(c1)
        if self.__color == 'yellow':
            print(c1)
            print(colored(cc, self.__color))
            print(c1)
        if self.__color == 'green':
            print(c1)
            print(c1)
            print(colored(cc, self.__color))

    def running(self):
        if self.__color == 'red':
            # print(colored(f'{self.__color} light is on', 'red'))
            self.colortraffic()
            time.sleep(7)
            print()

        elif self.__color == 'yellow':
            # print(colored(f'{self.__color} light is on', 'yellow'))
            self.colortraffic()
            time.sleep(2)
            print()

        elif self.__color == 'green':
            # print(colored(f'{self.__color} light is on', 'green'))
            self.colortraffic()
            time.sleep(5)
            print()


while True:
    for i in range(len(lights)):
        if lights[i - 1] == 'red' or lights[i - 1] == 'yellow' or lights[i - 1] == 'green' and i != 'yellow':
            first = TrafficLight(lights[i])
            first.running()
        else:
            print("ERROR DON'T TOUCH traffic light")
            exit()

"""
   @@@@@
 @@@@@@@@@
@@@@@@@@@@@
 @@@@@@@@@
  @@@@@@@
   .....
 .........
...........
 .........
  .......
   .....
 .........
...........
 .........
  .......

   .....
 .........
...........
 .........
  .......
   @@@@@
 @@@@@@@@@
@@@@@@@@@@@
 @@@@@@@@@
  @@@@@@@
   .....
 .........
...........
 .........
  .......

   .....
 .........
...........
 .........
  .......
   .....
 .........
...........
 .........
  .......
   @@@@@
 @@@@@@@@@
@@@@@@@@@@@
 @@@@@@@@@
  @@@@@@@
"""
