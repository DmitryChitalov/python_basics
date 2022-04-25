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


class Cars:
    speed = None
    color = None
    name = None
    is_police = False

    def __init__(self, speed, color, name, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return 'Car is started and'

    def stop(self):
        return 'Car is stopped and'

    def turn(self, direction):
        return 'Car is turn' + direction


class TownCar(Cars):
    family = None
    def __init__(self, name, color, speed, family = True):
        super().__init__(name, color, speed)
        self.family = family


class SportCar(Cars):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed)


class WorkCar(Cars):
    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)


class PoliceCar(Cars):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed, True)


ford = TownCar(f'with speed {50} km/h running away', 'Yellow color', 'Ford')
ford1 = TownCar(f'with speed {190} km/h running away', 'Blue color', 'Ford')
ford2 = TownCar(f'with speed {180} km/h running away', 'Red color', 'Ford')
police = PoliceCar(f'with speed {180} km/h running away', 'White/Blue color', 'BMW')

print(police.name, police.speed, ford.is_police)
print(ford.color, ford.name, ford.speed, 'and then', ford.turn(direction=' to the right'))
print(ford2.name, ford.color, ford2.speed, 'and then', ford.turn(direction=' to the left'), ford1.is_police)
print(ford2.name, ford2.color, ford2.speed, ford2.is_police)
print(ford1.go(), ford1.name, ford2.color, ford1.speed, police.is_police)
print(police.name, police.color, police.speed, police.is_police, police.turn(direction=' to the right'))
print(ford.go(), ford.color, police.name, police.speed, ford.turn(direction=' to the right'))