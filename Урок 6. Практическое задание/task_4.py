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
    """info"""
    speed: int
    color: str
    name: str
    is_police: bool = False

    def __init__(self, speed: int, color: str, name: str) -> None:
        """info"""
        self.speed = speed
        self.color = color
        self.name = name

    def start(self):
        """info"""
        print(f"{self.name}: старт")

    def stop(self):
        """info"""
        print(f"{self.name}: стоп")

    def turn(self, direction: str):
        """info"""
        print(f"{self.name}: поворот - {direction}")

    def show_speed(self):
        """info"""
        print(f"{self.name}: скорость = {self.speed} км/ч")


class TownCar(Car):
    """info"""
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f"{self.name}: превышение скорости")


class SportCar(Car):
    """info"""



class WorkCar(Car):
    """info"""
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f"{self.name}: превышение скорости")


class PoliceCar(Car):
    """info"""
    is_police: bool = True


cars = [
    SportCar(240, 'red', 'Audi'),
    TownCar(180, 'silver', 'Kia'),
    WorkCar(80, 'white', 'Golf'),
    PoliceCar(170, 'black', 'Ford'),
]

cars[0].start()
cars[0].turn("направо")
cars[0].stop()

for car in cars:
    car.show_speed()
