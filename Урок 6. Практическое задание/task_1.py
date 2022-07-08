import time

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


class TrafficLight:
    __color = ["красный", "желтый", "зеленый"]

    def __init__(self, times):
        self.__times = times

    def running(self):
        """
        Функция выполняет переключение светофора, временные интервалы задаются в контрукторе класса
        :return:
        Пример запуска: <Object <TrafficLight> class>.running()
        """
        try:
            for num, el in enumerate(self.__color):
                print(f"Switch on to : {el}")

                if num == 0:
                    time.sleep(self.__times[0])
                elif num == 1:
                    time.sleep(self.__times[1])
                else:
                    time.sleep(self.__times[2])

        except BaseException as e:
            print(f"General error: {e}")


my_TrafficLight = TrafficLight([7, 2, 14])
my_TrafficLight.running()
