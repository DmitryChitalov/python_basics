import time


class TrafficLight:
    def __init__(self):
        self.__color = 'красный'

    def running(self):
        while True:
            if self.__color == 'красный':
                print('красный свет')
                time.sleep(7)
                self.__color = 'желтый'
            elif self.__color == 'желтый':
                print('желтый свет')
                time.sleep(2)
                self.__color = 'зеленый'
            elif self.__color == 'зеленый':
                print('зеленый свет')
                time.sleep(5)
                self.__color = 'красный'


traffic_light = TrafficLight()
traffic_light.running()