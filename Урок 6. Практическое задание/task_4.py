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
        self.is_polise = is_police
    def go(self):
        print(f"Машина поехала {self.name}")
    def stop(self):
        print(f"Машина остановилась {self.name}")
    def turn(self, direction):
        print(f"Машина {self.name} повернула {direction}")
    def show_speed(self):
        print(f"скорость {self.name} движения {self.speed}")

class TownCar(Car):
    def show_speed(self):
        print(f"Скорость свыше 60 км/ч")

class SportCar(Car):
    def type_car(self):
        print(f"Спотривная машина {self.name} {self.color}")

class WorkCar(Car):
    def show_speed(self):
        print(f"Скорость свыше 40 км/ч")

class PoliceCar(Car):
    def type_car(self):
        print(f"Полицейская машина {self.name} {self.is_police}")

town_car = TownCar(120, 'белая', 'Машина для города', False)
sport_car = SportCar(180, 'Желтая', 'Спортивная машина', False)
work_car = WorkCar(70, 'Зеленая', 'Рабочая машина', False)
polise_car = PoliceCar(100, 'Синяя', 'Полицейская машина', False)

print(town_car.name)
print()
sport_car.show_speed()
print()
work_car.show_speed()
print(work_car.name, work_car.color)
print()
polise_car.show_speed()
sport_car.turn('налево')








