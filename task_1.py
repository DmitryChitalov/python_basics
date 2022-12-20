import time

class TrafficLight:
    def _init_(self, color):
        self.__color = color

    def running(self):
        color = {'красный': 7, 'желтый': 2, 'зеленый': 9}
        for key, value in color.items():
            print(f"Светофор переключился на {key} цвет")
            time.sleep(value)

a = TrafficLight()
a.running()