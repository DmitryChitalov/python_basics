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
    is_police = None

    def __init__(self, speed, color, name):
        try:
            self.speed = float(speed)

            self.name = name
            self.color = color
        except ValueError:
            raise TypeError(f'Задайте параметры с корректными типами данных:\n`speeed` - `float`')

    def go(self):
        return "Автомобиль в движении"

    def stop(self):
        return "Автомобиль остановился"

    def turn(self, direction):
        return f'Автомобиль повернул в направлении: {direction}'

    def show_speed(self):
        return f'Текущая скорость автомобиля: {self.speed} км/ч'

class TownCar(Car):
    is_police = False

    def show_speed(self):
        if self.speed > 40:
            message = f'Текущая скорость автомобиля: {self.speed} км/ч превышает допустимый предел в 40 км/ч'
        else:
            message = f'Текущая скорость автомобиля: {self.speed} км/ч'
        return message

class WorkCar(Car):
    is_police = False

    def show_speed(self):
        if self.speed > 60:
            message = f'Текущая скорость автомобиля: {self.speed} км/ч превышает допустимый предел в 60 км/ч'
        else:
            message = f'Текущая скорость автомобиля: {self.speed} км/ч'
        return message

class SportCar(Car):
    is_police = False

class PoliceCar(Car):
    is_police = True


police_car_1 = PoliceCar(100, 'black', 'Патрульная машика х999хх27')
print(police_car_1.name)
print(police_car_1.is_police)
print(police_car_1.speed)
print(police_car_1.color)
print(police_car_1.go())
print(police_car_1.turn('left'))


dedovoz = TownCar(50, 'white', 'Lada Calina a111aa27')
print(dedovoz.show_speed())

musorovoz = WorkCar(40, 'orange', 'Камаз м222мм27')
print(musorovoz.show_speed())



