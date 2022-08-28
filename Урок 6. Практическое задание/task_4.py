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
        return f'{self.name} Поехала\n'

    def stop(self):
        return f'{self.name} Остановилась\n'

    def turn(self, direction):
        return f'{self.name} Повернула {direction}\n'

    def show_speed(self):
        return f'Текущая скорость - {self.speed}\n'


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            return f'Превышение скорости - {self.speed}\n'
        else:
            return f'Скорость в норме - {self.speed} \n'


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            return f'Превышение скорости - {self.speed} \n'
        else:
            return f'Скорость в норме - {self.speed}\n'


class PoliceCar(Car):
    pass


cars = TownCar(70, 'черная', 'BMW', True)
print(cars.go(), cars.turn('налево'), cars.show_speed(), cars.stop())

cars = WorkCar(35, 'красная', 'VW', False)
print(cars.go(), cars.turn('направо'), cars.show_speed(), cars.stop())

cars = SportCar(110, 'белая', 'Merscedes', False)
print(cars.go(), cars.turn('направо'), cars.turn('налево'), cars.show_speed(), cars.stop())

cars = PoliceCar(90, ',синяя', 'AUDI', True)
print(cars.go(), cars.turn('налево'), cars.turn('направо'), cars.show_speed(), cars.stop())