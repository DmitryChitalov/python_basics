from time import sleep
class TrafficLight:
    __color = ["красный", "желтый", "зеленный"]
    def running(self):
        print(TrafficLight.__color[0])
        sleep(7)
        print(TrafficLight.__color[1])
        sleep(2)
        print(TrafficLight.__color[2])
        sleep(7)

a = TrafficLight()
a.running()