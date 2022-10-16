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
from os import system, name as osname


def cls():
    system('cls' if osname == 'nt' else 'clear')


class Car:

    def __init__(self, speed, color, name, is_police=0):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        if self.is_police:
            return print(f"Полицейская машина {self.name}, цвет {self.color},  движется.")
        else:
            return print(f"Машина {self.name}, цвет {self.color} движется.")

    def stop(self):
        return print(f"Машина {self.name} остановилась.")

    def turn(self, direction):
        return print(f"Машина {self.name} повернула на{direction}.")

    def show_speed(self):
        return print(f"Ваша скорость {self.speed} км/ч")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return print(f"Вы превысили скорость 40 км/ч. Ваша скорость {self.speed}")
        else:
            return print(f"Ваша скорость {self.speed}.")


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return print(f"Вы превысили скорость 60 км/ч. Ваша скорость {self.speed}")
        else:
            return print(f"Ваша скорость {self.speed}.")


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


cls()
print("---------------------------------------------------")
oka1 = TownCar(40, "зеленый", "Ока1")
oka1.go(), oka1.show_speed(), oka1.turn("лево"), oka1.turn("право"), oka1.stop()
print("---------------------------------------------------")
oka2 = TownCar(60, "зеленый", "Ока2")
oka2.go(), oka2.show_speed(), oka2.turn("лево"), oka2.turn("право"), oka2.stop()
print("---------------------------------------------------")
gaz1 = WorkCar(60, "желтый", "Газель1")
gaz1.go(), gaz1.show_speed(), gaz1.turn("лево"), gaz1.turn("право"), gaz1.stop()
print("---------------------------------------------------")
gaz2 = WorkCar(70, "желтый", "Газель2")
gaz2.go(), gaz2.show_speed(), gaz2.turn("лево"), gaz2.turn("право"), gaz2.stop()
print("---------------------------------------------------")
ferrari = SportCar(200, "Красный", "Ferrari")
ferrari.go(), ferrari.show_speed(), ferrari.turn(
    "лево"), ferrari.turn("право"), ferrari.stop()
print("---------------------------------------------------")
uaz = PoliceCar(100, "белый", "УАЗ", 1)
uaz.go(), uaz.show_speed(), uaz.turn("лево"), uaz.turn("право"), uaz.stop()
print("---------------------------------------------------")
