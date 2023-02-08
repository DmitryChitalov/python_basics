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
    speed: int
    tmp_speed: int
    color: str
    name: str
    is_police = False

    def __init__(self, my_speed, my_color, my_name):
        self.speed = my_speed
        self.tmp_speed = my_speed
        self.color = my_color
        self.name = my_name

    def go(self):
        print("Машина поехала")
        self.speed = self.tmp_speed

    def stop(self):
        print("Машина остановилась")
        self.speed = 0

    def turn(self, direction: str):
        print(f"Машина повернула {direction}")

    def show_speed(self):
        pass
        print(f"Скорость машины: {self.speed}км/ч.")


class TownCar(Car):

    def show_speed(self):
        print(f"Скорость машины: {self.speed}км/ч.")
        if self.speed > 60:
            print(f"Внимание! Скорость 60 км/ч. превышена! Необходимо снизить скорость!")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(f"Скорость машины: {self.speed}км/ч.")
        if self.speed > 40:
            print(f"Внимание! Скорость 40 км/ч. превышена! Снизте скорость!")


class PoliceCar(Car):
    is_police = True


my_town_car = TownCar(70, "Красный", "ЗАЗ")
if my_town_car.is_police:
    print("Это полицейская машина")
else:
    print("Это не полицейская машина")

print(f"{my_town_car.color} {my_town_car.name}")
my_town_car.show_speed()
my_town_car.stop()
my_town_car.show_speed()
my_town_car.go()
my_town_car.show_speed()


my_police_car = PoliceCar(170, "Синий", "ЗАЗ")
if my_police_car.is_police:
    print("Это полицейская машина")
else:
    print("Это не полицейская машина")

print(f"{my_police_car.color} {my_police_car.name}")
my_police_car.show_speed()
my_police_car.stop()
my_police_car.show_speed()
my_police_car.turn("направо")
my_police_car.go()
my_police_car.show_speed()
