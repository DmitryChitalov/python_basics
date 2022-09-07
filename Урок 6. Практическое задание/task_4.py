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
import random


class Car:
    speed = 0
    color = "white"
    name = "BMW"
    is_police = False

    def go(self):
        self.speed = random.randrange(0, 180)
        self.show_speed()
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def show_speed(self):
        print(f"Скорость данного автомобиля достигает: {self.speed}")

    def turn(self, direction):
        if self.speed > 100:
            print(f"Полегче на поворотах {direction}")
        else:
            print(f"Машина повернула {direction}")

    def __init__(self, speed=0, color="white", name="BMW", is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def __str__(self):
        return str(f"Скорость: {self.speed}\n"
              f"Цвет: {self.color}\n"
              f"Марка: {self.name}\n"
              f"Полицейский : {'да' if self.is_police else 'нет'}")

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Превышение скоростного режима городского транспорта")


class SportCar(Car):
    def __init__(self):
        super().__init__()
        self.name = "Porsche 911"


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Превышение скоростного режима рабочего транспорта")


class PoliceCar(Car):
    def __init__(self):
        super().__init__()
        self.is_police = True
        self.name = "Chevrolet Cruze"

town_car = TownCar(0, "Синий", "TownCar")
town_car.go()
town_car.turn("направо")
town_car.stop()
print(f"{town_car}\n")

work_car = WorkCar(0, "Зеленый", "WorkCar")
work_car.go()
work_car.turn("налево")
work_car.stop()
print(f"{work_car}\n")

sport_car = SportCar()
sport_car.go()
sport_car.turn("направо")
sport_car.stop()
print(f"{sport_car}\n")

police_car = PoliceCar()
police_car.go()
police_car.turn("налево")
police_car.stop()

print(police_car.name)
police_car.show_speed()
print(police_car.speed)
print(police_car.color)

