from time import sleep

class TrafficLight:
    __color = {'Красный': 7, 'Желтый': 2, 'Зеленый': 7}

    def running(self):
        for key, value in TrafficLight.__color. items():
            print(f'Светофор переключился в режим {key}')
            sleep(value)

TL = TrafficLight()
TL.running()