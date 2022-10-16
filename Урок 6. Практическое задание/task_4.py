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

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        if self.is_police:
            return f"Полицейская машина {self.name}, цвет {self.color},  движется."
        else:
            return f"Машина {self.name}, цвет {self.color} движется."

    def stop(self):
        return f"Машина {self.name} остановилась."

    def turn(self, direction):
        return f"Машина {self.name} повернула на{direction}."

    def show_speed(self):
        return f"Ваша скорость {self.speed} км/ч"


class TownCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f"Вы превысили скорость 40 км/ч. Ваша скорость {self.speed}"
        else:
            return f"Ваша скорость {self.speed}."


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f"Вы превысили скорость 60 км/ч. Ваша скорость {self.speed}"
        else:
            return f"Ваша скорость {self.speed}."


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


cls()
t = TownCar(40, "зеленый", "Ока", 0)
print(t.go())
print(t.show_speed())
print(t.turn("лево"))
print(t.turn("право"))
print(t.stop(), "\n")

t = TownCar(60, "зеленый", "Ока", 0)
print(t.go())
print(t.show_speed())
print(t.turn("лево"))
print(t.turn("право"))
print(t.stop(), "\n")

w = WorkCar(60, "желтый", "Газель", 0)
print(w.go())
print(w.show_speed())
print(w.turn("лево"))
print(w.turn("право"))
print(w.stop(), "\n")

w = WorkCar(70, "желтый", "Газель", 0)
print(w.go())
print(w.show_speed())
print(w.turn("лево"))
print(w.turn("право"))
print(w.stop(), "\n")

s = SportCar(200, "Красный", "Ferrari", 0)
print(s.go())
print(s.show_speed())
print(s.turn("лево"))
print(s.turn("право"))
print(s.stop(), "\n")

p = PoliceCar(100, "белый", "UAZ", 1)
print(p.go())
print(p.show_speed())
print(p.turn("лево"))
print(p.turn("право"))
print(p.stop(), "\n")
