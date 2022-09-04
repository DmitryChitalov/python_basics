from time import sleep


class TrafficLight:

    def __init__(self, color):
        self.__color = color

    def running(self):
        for key, value in self.__color.items():
            print(key)
            sleep(value)


a = TrafficLight(color={"red": 7, "yellow": 2, "green": 15})
a.running()
