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
    _is_police = False
    def __init__(self, color, name):
        self.color = color
        self.name = name

    def go(self, other_speed = 0):
        print(other_speed)
        if other_speed != 0:
            self.speed = other_speed
        else:
            self.speed = 10

    def stop(self):
        self.stop = 0

    def turn(self, direction):
        print(f"машина повернула на: {direction}")
    def show_speed(self):
        print(f"текущую скорость автомобиля: {self.speed}")


class TownCar(Car):

    def show_speed(self):
        super
        if self.speed > 60:
            print("превышении скорости!!!")

class SportCar(Car):
    pass

class WorkCar(Car):

    def show_speed(self):
        super
        if self.speed > 40:
            print("превышении скорости!!!")
class PoliceCar(Car):

    def __init__(self):
        super
        _is_police = True



obj = WorkCar("red", "bmw")
obj.go(70)
obj.show_speed()