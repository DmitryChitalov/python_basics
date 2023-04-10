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
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"машина {self.name} поехала")

    def stop(self):
        print(f"машина {self.name} остановилась")

    def turn(self, direction):
        print(f"машина {self.name} повернула {direction}")

    def show_speed(self):
        print(f"Скорость авто: {self.speed}")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"превышении скорости свыше 60")
        else:
            print(f"Скорость авто: {self.speed}")

class SportCar(Car):
    def type_car(self):
        print(f"{self.name} {self.color} SportCar")


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"превышении скорости свыше 40")
        else:
            print(f"Скорость авто: {self.speed}")

class PoliceCar(Car):
    def type_car(self):
        if self.is_police is True:
            print(f"{self.name} PoliceCar")
        else:
            print(f"{self.name} Не полицейский авто")


obj_1 = Car(80, "red", "toyota")
print(obj_1.name)
print(obj_1.color)
print(obj_1.speed)

obj_1.go()
obj_1.show_speed()
obj_1.turn("налево")
obj_1.turn("направо")
obj_1.stop()

speed_workcar = int(input("Введите скорость другого авто WorkCar: "))
obj_2 = WorkCar(speed_workcar, "blue", "opel")
obj_2.show_speed()

speed_towncar = int(input("Введите скорость другого авто TownCar: "))
obj_3 = TownCar(speed_towncar, "blue", "opel")
obj_3.show_speed()

speed_sportcar = int(input("Введите скорость другого авто SportCar: "))
obj_4 = SportCar(speed_sportcar, "black", "lada")
obj_4.show_speed()

obj_5 = PoliceCar(60, "white", "BMW", True)
obj_5.show_speed()
obj_5.type_car()
