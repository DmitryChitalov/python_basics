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
from time import sleep
from datetime import datetime


class TrafficLight:
    _states = {'красный': 7, 'желтый': 2, 'зеленый': 10}
    _color = ''

    def run(self):
        for color, sw_time in self._states.items():
            self._color = color
            start_state_time = datetime.now()

            print(f"Цвет светофора сменился на '{self._color}' "
                  f"на {sw_time} секунд")
            sleep(sw_time)

            print(f"Цвет светофора изменится на '{self._color}' через "
                  f"{(datetime.now() - start_state_time).seconds} секунд")

if __name__ == '__main__':
    tl = TrafficLight()
    tl.run()
