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
    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Car "{self.name}" went.')

    def stop(self):
        print(f'Car "{self.name}" stopped.')

    def turn(self, direction: str):
        print(f'Car "{self.name}" turned {direction}.')

    def show_speed(self):
        print(f'Speed of car "{self.name}" is {self.speed}.')


class TownCar(Car):
    def show_speed(self):
        message = f'Speed of car "{self.name}" is {self.speed}.'
        if self.speed > 60:
            message += f' Attention! The speed of the car "{self.name}" is above 60 km.'
        print(message)


class WorkCar(Car):
    def show_speed(self):
        message = f'Speed of car "{self.name}" is {self.speed}.'
        if self.speed > 40:
            message += f' Attention! The speed of the car "{self.name}" is above 40 km.'
        print(message)


class PoliceCar(Car):
    def __init__(self, speed: int, color: str, name: str, is_police: bool = True):
        super().__init__(speed, color, name, is_police)


class SportCar(Car):
    pass


car_1 = TownCar(speed=10, color='red', name='Toyota', is_police=False)
car_1.show_speed()
car_1.speed = 70
car_1.show_speed()

car_2 = PoliceCar(speed=100, color='blue', name='Lexus')
print(car_2.is_police)
car_2.show_speed()
car_2.go()
car_2.turn('right')
car_2.stop()

car_1 = WorkCar(speed=25, color='yellow', name='JBC', is_police=False)
car_1.show_speed()
car_1.speed = 45
car_1.show_speed()