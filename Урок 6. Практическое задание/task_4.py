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
    def __init__(self, *args):
        self.speed = int(args[0])
        self.color = args[1]
        self.name = args[2]
        self.is_police = args[3]

    def go(self):
        print(f"Car {self.name} go")
    def stop(self):
        print(f"Car {self.name} stop")
    def turn(self, direction):
        print(f"Car {self.name} turn to the {direction}")
    def show_speed(self):
        return self.speed

class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if 60 < self.speed:
            print("Too much speed for town car.")
        else:
            return self.speed

class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if 40 < self.speed:
            print("Too much speed for work car.")
        else:
            return self.speed

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)

TC = TownCar(55, "black", "Prius")
SC = SportCar(90, "red", "silvia")
WC = WorkCar(60, "yellow", "hyundai")
PC = PoliceCar(100, "white", "bmw")

print(TC.name)
print(SC.name)
print(WC.name)
print(PC.name)

print(TC.show_speed())
print(SC.show_speed())
print(WC.show_speed())
print(PC.show_speed())
