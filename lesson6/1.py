"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд,
второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и завершать скрипт.
"""
import itertools
import time


class TrafficLight:
    __color: str
    __timing: dict

    def __init__(self, red_time: int = 7, yellow_time: int = 2, green_time: int = 5):
        self.__timing = {
            "red": red_time,
            "yellow": yellow_time,
            "green": green_time
        }

    def running(self):
        for mode, timer in itertools.cycle(self.__timing.items()):
            self.__color = mode

            for second in range(timer):
                print(f"{self} [{second + 1}]")
                time.sleep(1)

    def __repr__(self):
        return f"Текущий режим = {self.__color}"


try:
    traffic_light = TrafficLight(7, 2, 5)
    traffic_light.running()
except KeyboardInterrupt:
    print("Exit the program")