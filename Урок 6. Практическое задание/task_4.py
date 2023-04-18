"""
Задание 4.

Реализуйте базовый класс Car. У данного класса должны быть следующие публичные атрибуты:
speed, color, name, is_police (булево).

А также публичные методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).

Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.

Добавьте в базовый класс публичный метод show_speed,
который должен показывать текущую скорость автомобиля.

Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        if self.speed != 0:
            print('Машина едет')

    def stop(self):
        if self.speed == 0:
            print('Машина остановилась')

    def turn(self, side):
        if side == 1:
            print('Машина поворачивает влево')
        if side == 2:
            print('Машина поворачивает вправо')


TownCar = Car(0, 'yello', 'Priora', '')
SportCar = Car(120, 'Red', 'Lambo', '')
WorkCar = Car(35, 'gray', 'gazelle', '')
PoliceCar = Car(200, 'hakky', 'bobik', '...')