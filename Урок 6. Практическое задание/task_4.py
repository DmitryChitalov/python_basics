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
    name: str
    color: str
    speed: float
    is_police: bool

    def __init__(self, name, color, speed):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = False

    def go(self):
        return f'The {self.name} started moving'

    def stop(self):
        return f'The {self.name} stopped moving'

    def turn(self, direction):
        return f'The {self.name} turned to the {direction}'

    def show_speed(self):
        return f'the speed equals {self.speed}'


class TownCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed)

    def show_speed(self):
        result = ''
        if self.speed > 60:
            result = "\nWARNING: Speeding!"
        return f'{super().show_speed()}{result}'


class WorkCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed)

    def show_speed(self):
        result = ''
        if self.speed > 40:
            result = "\nWARNING: Speeding!"
        return f'{super().show_speed()}{result}'


class PoliceCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed)
        self.is_police = True


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


audi = SportCar('Audi', 'Black', 100)
opel = TownCar('Opel', 'White', 30)
hyundai = WorkCar('Hyundai', 'Gold', 70)
toyota = PoliceCar('Toyota', 'Blue', 110)

print(f'{opel.turn("Left")} on the first crossroads')
print(f'{opel.turn("Right")} on the corner')
print(f'{audi.go()}, then after two hours {audi.stop()}')
print(f'{hyundai.go()} with {hyundai.show_speed()}')
print(f'{hyundai.name} is {hyundai.color}')
print(f'Is {audi.name} a police car? {audi.is_police}')
print(f'Is {toyota.name} a police car? {toyota.is_police}')
print(audi.show_speed().capitalize())
print(opel.show_speed().capitalize())
print(toyota.show_speed().capitalize())
