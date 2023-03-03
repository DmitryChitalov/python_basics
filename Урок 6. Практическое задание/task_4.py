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

# pylint: disable=missing-class-docstring, missing-function-docstring,invalid-name


class Car:
    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} поехала.')

    def stop(self):
        print(f'Машина {self.name} остановилась.')

    def turn(self, direction: str):
        print(f'Машина {self.name} повернула {direction}.')

    def show_speed(self):
        print(f'Текущая скорость {self.color} {self.name} - {self.speed}.')


class TownCar(Car):
    def show_speed(self):
        message = f'Скорость {self.name} - {self.speed}.'
        if self.speed > 60:
            message += f' Скорость {self.color} {self.name} превышена.'
        print(message)


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        message = f'Скорость {self.name} - {self.speed}.'
        if self.speed > 40:
            message += f' Скорость {self.color} {self.name} превышена.'
        print(message)


class PoliceCar(Car):
    def __init__(self, speed: int, color: str, name: str, is_police: bool = True):
        super().__init__(speed, color, name, is_police)


car_1 = TownCar(speed=80, color='синий', name='Audi', is_police=False)
car_2 = PoliceCar(speed=90, color='черный', name='BMW', is_police=True)
car_3 = WorkCar(speed=25, color='белый', name='Toyota', is_police=False)

car_1.show_speed()
car_2.show_speed()
car_3.show_speed()

car_1.stop()

car_2.go()
car_2.turn('на право')
print(f'{car_2.name} - полицейский {car_2.is_police}')

car_1.speed = 40
car_1.turn('на лево')
car_1.show_speed()
