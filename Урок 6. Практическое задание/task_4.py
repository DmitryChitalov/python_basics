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

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f"машина {self.name} поехала"

    def stop(self):
        return f"\nМашина {self.name} остановилась"

    def turn(self, direction):
        return f"\nМашина {self.name} повернула {direction}"

    def show_speed(self):
        return f"\nТекущая скорость автомобиля {self.speed} км\ч"


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f"\nВаша скорость выше допустимой - {self.speed} км\ч. Пожалуйста сбавьте обороты"
        else:
            return f"Скорость автомобиля - {self.name} в норме"


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f"\nВаша скорость выше допустимой - {self.speed} км\ч. Пожалуйста сбавьте обороты"
        else:
            return f"\nСкорость автомобиля - {self.name} в норме"


class PoliceCar(Car):
    pass


t = TownCar("Toyota", 85, "Белая", False)
print("1:\n" + t.color, t.go(), t.show_speed(), t.turn("на лево"), t.turn("на право"), t.stop())

s = SportCar("Mercedes", 200, "Черная", False)
print("2:\n" + s.color, s.go(), s.show_speed(), s.turn("на лево"), s.stop())

w = WorkCar("Opel", 40, "Красная", False)
print("3:\n" + w.color, w.go(), w.show_speed(), w.turn("на право"), w.stop())

p = PoliceCar("BMW", 59, "Синяя", False)
print("4:\n" + p.color, p.go(), p.show_speed(), p.turn("на право"), p.turn("на лево"), p.stop())