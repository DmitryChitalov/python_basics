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
    speed: int
    color: str
    name: str
    is_police: bool = False

    def __init__(self, speed: int, color: str, name: str) -> None:
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print(f"{self.name}: start")

    def stop(self):
        print(f"{self.name}: stop")

    def turn(self, direction: str):
        print(f"{self.name}: turn - {direction}")

    def show_speed(self):
        print(f"{self.name}: speed = {self.speed} km/h")


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f"{self.name}: speeding")


class SportCar(Car):
    pass


class WorkerCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f"{self.name}: speeding")


class PoliceCar(Car):
    is_police: bool = True


cars = [
    SportCar(300, 'red', 'Pagani'),
    TownCar(200, 'white', 'Toyota'),
    WorkerCar(90, 'blue', 'Mercedes'),
    PoliceCar(190, 'black', 'Honda'),
]

cars[0].go()
cars[0].turn('to the left')
cars[0].stop()

for car in cars:
    car.show_speed()
