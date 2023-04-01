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


class Car:
    speed = 70
    color = 'red'
    name = 'Mazda'
    is_police = True
    random_turn = random.choice(x)

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


town_car = TownCar()
sport_car = SportCar()
work_car = WorkCar()
police_car = PoliceCar()

town_car.show_speed()
work_car.show_speed()
sport_car.show_speed()
police_car.turn()
