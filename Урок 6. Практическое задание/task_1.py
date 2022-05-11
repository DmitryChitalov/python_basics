from time import sleep


class TrafficLight:
    __color = {'Красный': 7, 'Желтый': 2, 'Зелёный': 10}

    def start(self):
        for key, value in self.__color.items():
            print(f"цвет сейчас - {key}")
            sleep(value)


a = TrafficLight()
a.start()
