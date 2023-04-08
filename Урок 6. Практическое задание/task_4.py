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
    is_police = False

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def go(self):
        return 'машина поехала'

    def stop(self):
        return 'машина остановилась'

    def turn(self, direction):
        if direction in ('налево', 'направо'):
            return f"машина повернула {direction}"

    def show_speed(self):
        return f"скорость {self.speed} км/ч"


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f"превышение скорости -  {self.speed} км/ч"
        else:
            return f"скорость {self.speed} км/ч"


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f"превышение скорости -  {self.speed} км/ч"
        else:
            return f"скорость {self.speed} км/ч"


class PoliceCar(Car):
    def is_police(self):
        return "полиция"


townCar = TownCar(name='Mazda', color='Синий')
workCar = WorkCar(name='Opel', color='Черный')
policeCar = PoliceCar(name='Lada', color='Белый')

townCar.speed = 92
workCar.speed = 30
policeCar.speed = 82

print(
    f"{townCar.color} {townCar.name} - {townCar.go()} {townCar.show_speed()} {townCar.turn('налево')} {townCar.turn('направо')}")
print(
    f"{workCar.color} {workCar.name} - {workCar.go()} {workCar.show_speed()} {workCar.turn('направо')} {workCar.turn('налево')}")
print(
    f"{policeCar.color} {policeCar.name} {policeCar.is_police()} - {policeCar.go()} {policeCar.show_speed()} {policeCar.turn('налево')} {policeCar.turn('направо')}")

townCar.speed = 103
workCar.speed = 10
policeCar.speed = 120

print(f"{townCar.color} {townCar.name} -  {townCar.show_speed()}  {townCar.turn('направо')} {townCar.stop()}")
print(f"{workCar.color} {workCar.name} -  {workCar.show_speed()} {workCar.stop()}")
print(
    f"{policeCar.color} {policeCar.name} {policeCar.is_police()} - {policeCar.show_speed()} {policeCar.turn('направо')} {policeCar.stop()}")
