from time import sleep

class TrafficLight:
    def __init__(self, color):
        self.__color_light = color

    def running(self):
        for i in self.__color_light:
            sleep(self.__color_light[i])
            print(i)

light = TrafficLight({"Красный": 7, "Желтый": 2, "Зеленый": 5})

light.running()