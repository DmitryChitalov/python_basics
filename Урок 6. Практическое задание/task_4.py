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
import random

x = ['Налево', 'Направо', 'Назад']
random_x = random.choice(x)


class Car:

    def __init__(self, speed, color, name, is_police, random_turn):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.random_turn = random_turn

    def go(self):
        print('машина поехала')

    def stop(self):
        print('машина остановилась')

    def turn(self):
        print(f'машина повернула {self.random_turn}')

    def show_speed(self):
        print(f'Текущая скорость автомобиля - {self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости')
        else:
            print('Превышения скорости нет')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Превышение скорости')
        else:
            print('Превышения скорости нет')


class PoliceCar(Car):
    pass


town_car = TownCar(60, 'red', 'Mazda', False, random_x)
sport_car = SportCar(90, 'blue', 'Opel', False, random_x)
work_car = WorkCar(30, 'black', 'Nissan', False, random_x)
police_car = PoliceCar(60, 'red', 'Mazda', True, random_x)

town_car.show_speed()
work_car.show_speed()
sport_car.show_speed()
police_car.turn()
