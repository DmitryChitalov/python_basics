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
from os import system, name as osname
from time import sleep
from colorama import Back, Style


def cls():
    system('cls' if osname == 'nt' else 'clear')


class TraficLite:
    __color = "RED", "YELLOW", "GREEN"

    def running(red_on, green_on, repit):
        cls()
        count_on_off = 0
        while count_on_off < repit:
            for el in TraficLite.__color:
                if el == "RED":
                    print(
                        f"Загорелся {Back.RED}красный{Style.RESET_ALL} сигнал светофора")
                    sleep(red_on)
                    cls()
                    print(
                        f"Загорелся {Back.YELLOW}желтый{Style.RESET_ALL} сигнал светофора")
                    sleep(2)
                    cls()
                elif el == "GREEN":
                    print(
                        f"Загорелся {Back.GREEN}зеленый{Style.RESET_ALL} сигнал светофора")
                    sleep(green_on)
                    cls()
                    print(
                        f"Загорелся {Back.YELLOW}желтый{Style.RESET_ALL} сигнал светофора")
                    sleep(2)
                    cls()
            count_on_off += 1


TraficLite.running(7, 5, 5)
