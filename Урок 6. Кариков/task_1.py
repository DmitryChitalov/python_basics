
from time import sleep


class TrafficLight:
    __color = {'Красный': 7, 'Желтый': 2, 'Зеленый': 4}

    @staticmethod
    def running() -> None:
        for key, value in TrafficLight.__color.items():
            print(f'Сейчас горит цвет: {key}')
            sleep(value)
            print(f'Переключаю цвет светофора')


if __name__ == '__main__':
    TrafficLight.running()
