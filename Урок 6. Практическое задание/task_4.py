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
    def __init__(self, speed, color, name, is_policy):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_poicy = is_policy

    def go(self):
        print(f' {self.name} поехала')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        print(f'Машина {self.name} поехала {direction}')

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.name} : {self.speed}')


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f'Скорость автомобиля {self.name} превышена')
        super().show_speed()


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Скорость автомобиля {self.name} превышена')
        super().show_speed()


class Sportcar(Car):
    def w_func(self):
        print(f'Классная машина {self.name} {self.color}')


class PoliceCar(Car):
    def c_func(self):
        print(f'Машина {self.color} {self.name} выехала на дежурство ')


tc1 = TownCar(55, 'green', 'mazda', False)
tc2 = TownCar(65, 'green', 'toyota', False)
wc1 = WorkCar(45, 'green', 'MAZ', False)
tc1.go()
tc1.show_speed()
tc2.show_speed()
wc1.show_speed()
sc1 = Sportcar(85, 'green', 'zaz', False)
tc2.turn('налево')
sc1.w_func()
pc1 = PoliceCar(75, 'white', 'priora', True)
pc1.c_func()
wc1.stop()