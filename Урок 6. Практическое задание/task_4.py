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
    color = ""
    name = ""
    is_police = False

    def __init__(self, color, name):
        self.color = color
        self.name = name

    def go(self):
        print(f"Car {self} поехала")

    def stop(self):
        print(f"Car {self} остановилась")

    def turn(self, direction="left"):
        print(f"Car {self} повернула {direction}")

    def __str__(self):
        return " ".join([self.name, "(", self.color, ")"])

    def show_speed(self):
        return (self.speed)


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"Текущая скорость {self.speed} > 60")
        else:
            print(self.speed)


class SportCar(Car):
    def __str__(self):
        return " ".join(["SportCar", self.name, "(", self.color, ")"])


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"Текущая скорость {self.speed} > 60")
        else:
            print(self.speed)


class PoliceCar(Car):
    is_police = True

    def __str__(self):
        return " ".join(["PoliceCar", self.name, "(", self.color, ")"])


p1 = PoliceCar("red", "mazda")
print(p1)
p1.go()
p1.speed = 100
print(p1.__dict__)
print(p1.is_police)
p1.show_speed()

p1 = TownCar("red", "mazda")
print(p1)
p1.go()
p1.speed = 100
print(p1.__dict__)
print(p1.is_police)
p1.show_speed()
p1.stop()
