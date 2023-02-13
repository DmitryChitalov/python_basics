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
        return f'Машина {self.name} поехала.'

    def stop(self):
        return f'Машина {self.name} остановилась.'

    def turn(self, direction):
        return f'Машина {self.name} повернула {direction}.'

    def show_speed(self):
        return f'Текущая скорость машины {self.name}: {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'Машина {self.name} превысила скорость на: {self.speed - 60} км/ч.'
        else:
            return f'Скорость машины {self.name} в норме допустимого.'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'Машина {self.name} превысила скорость на: {self.speed - 40} км/ч.'
        else:
            return f'Скорость машины {self.name} в норме допустимого.'


class PoliceCar(Car):
    pass


town = TownCar(84, 'blue', 'BMW')
print(town.go(), town.show_speed(), town.turn('налево'), town.turn('направо'), town.stop())

sport = SportCar(245, 'red', 'Ferarri')
print(sport.go(), sport.show_speed(), sport.turn('налево'), sport.stop())

work = WorkCar(40, 'yellow', 'Peugeot')
print(work.go(), work.show_speed(), work.turn('направо'), work.stop())

police = PoliceCar(90, 'yellow', 'Skoda', True)
print(police.go(), police.show_speed(), police.turn('направо'), police.stop())
