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

    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'\n{self.name} begin to ride'

    def stop(self):
        return f'\n{self.name} stoped'

    def turn(self, direction):
        return f'\n{self.name} turn {direction}'

    def show_speed(self):
        return f'\n{self.speed} - current speed'


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            return f'\n{self.speed} km/ph is over speed'
        else:
            return f'\n{self.speed} km/ph is normal speed'


class SportCar(Car):
    pass

class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            return f'\n{self.speed} km/ph is over speed'
        else:
            return f'\n{self.speed} km/ph is normal speed'

class PoliceCar(Car):
    pass

a = TownCar(59, 'Lamborgini', True)
print(a.go(), a.turn('left'), a.show_speed(), a.stop())

a = SportCar(200, 'Mazeratti', True)
print(a.go(), a.turn('right'), a.show_speed(), a.stop())

a = WorkCar(55, 'Mini', False)
print(a.go(), a.turn('into the tunnel'), a.show_speed(), a.stop())

a = PoliceCar(400, 'Ferrari', False)
print(a.go(), a.turn('left'), a.turn('rigth'), a.turn('around'), a.show_speed(), a.stop())