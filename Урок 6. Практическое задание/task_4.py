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
    speed = 0
    color = None
    name = None
    is_police = False

    def __init__(self, color, name):
        self.color = color
        self.name = name

    def go(self, speed):
        self.speed = speed
        return 'Машина поехала'

    def stop(self):
        self.speed = 0
        return 'Машина остановилась'

    def turn(self, direction):
        return f"Машина повернула на {direction}"

    def show_speed(self):
        return f"Скорость: {self.speed}"

    def __str__(self):
        return f"Машина:{self.name} Цвет:{self.color} Полиция:{'Да' if self.is_police else 'Нет'} "


class TownCar(Car):
    def show_speed(self):
        return f"Превышении скорости {self.speed}" if self.speed > 60 else self.speed


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        return f"Превышении скорости: {self.speed}" if self.speed > 40 else f"Скорость: {self.speed}"


class PoliceCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name)
        self.is_police = True


townCar = TownCar("red", "lada")
print(townCar)
print(townCar.go(80))
print(townCar.show_speed())
print(townCar.turn('право'))
print(townCar.stop())

sportCar = SportCar("green", "mazda")
print(sportCar)
print(sportCar.go(100))
print(sportCar.show_speed())
print(sportCar.stop())

workCar = WorkCar("red", "nisan")
print(workCar)
print(workCar.go(45))
print(workCar.show_speed())
print(workCar.turn('право'))
print(workCar.stop())

policeCar = PoliceCar("blue", "bmw")
print(policeCar)
print(policeCar.go(80))
print(policeCar.show_speed())
print(policeCar.stop())
