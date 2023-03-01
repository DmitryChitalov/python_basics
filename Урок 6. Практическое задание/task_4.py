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
        print(f"Машина {self.name} движется")

    def stop(self):
        print(f"Машина {self.name} остановилась")

    def turn(self, direction):
        print(f"Машина {self.name} повернула {direction}")

    def show_speed(self):
        print(f"Скорость машины {self.name}: {self.speed} км/ч")


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print("Скоростной лимит привышен!")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print("Скоростной лимит привышен!")


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=True)


town_car = TownCar(70, "зеленый", "Honda")
sport_car = SportCar(120, "коасный", "Ferrari")
work_car = WorkCar(45, "черный", "Ford")
police_car = PoliceCar(100, "белая с синей полосой", "ВАЗ")

print(town_car.color, town_car.name, town_car.is_police)
town_car.go()
town_car.show_speed()
town_car.turn("на лево")
town_car.stop()

print(sport_car.color, sport_car.name, sport_car.is_police)
sport_car.go()
sport_car.show_speed()
sport_car.turn("на право")
sport_car.stop()

print(work_car.color, work_car.name, work_car.is_police)
work_car.go()
work_car.show_speed()
work_car.turn("на право")
work_car.stop()

print(police_car.color, police_car.name, police_car.is_police)
police_car.go()
police_car.show_speed()
police_car.turn("на лево")
police_car.stop()
