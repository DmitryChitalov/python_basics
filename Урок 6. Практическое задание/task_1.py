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


import random
from time import sleep


class TrafficLight:
    """Класс - образец рабочего светофора"""
    __color: str

    def running(self, color: list):
        """Метод запуска"""
        self.__color = color[0]
        time_sleep = color[1]

        return f"Сейчас загорелся {self.__color} свеи и он будет гореть " \
                f"{time_sleep} секунд(ы)"


dict_light = {
    'Красный': 7,
    "Желтый": 2,
    "Зеленый": random.randint(4, 8)
}

traffic = TrafficLight()

for el, time in dict_light.items():
    print(traffic.running([el, time]))
    sleep(time)
