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
    def __init__(self, speed, name, is_police):
        self.speed = speed
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Машина {self.name} поехала")

    def stop(self):
        print(f"Машина {self.name} остановилась")

    def turn(self, direction):
        print(f"Машина {self.name} повернула - > {direction}")

    def show_speed(self):
        print(f"Текущая скорость автомобиля {self.name}: {self.speed} км/час")
        print()

    def __str__(self):
        print(f"{type(self).__name__}(name={self.name}, speed={self.speed}, is_police={self.is_police}")


class TownCar(Car):
    def __init__(self, speed, name):
        super().__init__(speed, name, False)

    def show_speed(self):
        if self.speed > 60:
            print(f"Автомобиль {self.name} превышает скорость в 60 км/час, текущая скорость: {self.speed}")
        else:
            print(f"Текущая скорость {self.name}: {self.speed} км/час")


class SportCar(Car):
    def __init__(self, speed, name):
        super().__init__(speed, name, False)


class WorkCar(Car):
    def __init__(self, speed, name):
        super().__init__(speed, name, False)

    def show_speed(self):
        if self.speed > 60:
            print(f"Автомобиль {self.name} превышает скорость в 40 км/час, текущая скорость: {self.speed}")
        else:
            print(f"Текущая скорость {self.name}: {self.speed} км/час")


class PoliceCar(Car):
    def __init__(self, speed, name):
        super().__init__(speed, name, True)


my_car = Car(10, "ВАЗ 2107", False)
my_car.__str__()
my_car.show_speed()


my_town_car = TownCar(25, "Kia Ceed")
my_town_car.__str__()
my_car.show_speed()

my_town_car.speed = 75
my_town_car.__str__()
my_town_car.show_speed()

my_work_car = WorkCar(42, "Mercedes GLK-300")
my_work_car.__str__()
my_work_car.show_speed()
