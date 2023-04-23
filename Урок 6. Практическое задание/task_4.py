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
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Машина {self.name} начала движение")

    def stop(self):
        print(f"Машина {self.name} прекратила движение")

    def turn(self, direction):
        if direction == "l":
            print(f"Машина {self.name}  повернула налево")
        elif direction == "r":
            print(f"Машина {self.name}  повернула направо")
        else:
            print(f"Машина {self.name}  продолжает движение прямо")

    def show_speed(self):
        print(f"Машина {self.name} едет со скоростью {self.speed} км/ч")


class TownCar(Car):
    def show_speed(self):
        if self.speed >= 60:
            print(f"TownCar {self.name} едет со скоростью {self.speed} км/ч, вы нарушаете правила "
                  f"ограничения скорости движения 60 км/ч")
        else:
            print(f"TownCar {self.name} едет со скоростью {self.speed} км/ч")


class SportCar(Car):
    def show_speed(self):
        print(f"SportCar {self.name} едет со скоростью {self.speed} км/ч")


class WorkCar(Car):
    def show_speed(self):
        if self.speed >= 40:
            print(f"WorkCar {self.name} едет со скоростью {self.speed} км/ч, вы нарушаете правила "
                  f"ограничения скорости движения 40 км/ч")
        else:
            print(f"WorkCar {self.name} едет со скоростью {self.speed} км/ч")


class PoliceCar(Car):
    def show_speed(self):
        print(f"PoliceCar {self.name} едет со скоростью {self.speed} км/ч")


a = TownCar(65, "белый", "AUDI", 0)
b = SportCar(95, "красный", "Mazda", 0)
c = WorkCar(45, "красный", "Mazda", 0)
d = PoliceCar(35, "синий", "УАЗ", 1)
a.go()
a.turn("l")
a.turn("r")
a.show_speed()
b.show_speed()
c.show_speed()
d.show_speed()
a.stop()
