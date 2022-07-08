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
    def __init__(self, speed, color, name, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехал')

    def stop(self):
        print(f'{self.name} остановился')

    def turn(self, directon):
        print(f'{self.name} повернул {directon}')

    def show_speed(self):
        print(f'Скорость {self.name} = {self.speed} км\ч')


class TownCar(Car):
    def show_speed(self):
        print(f'Автомобиль {self.name}: ', end='')
        if self.speed > 60:
            print(f'превышает скорость!')
        print(f'Скорость = {self.speed}')


class WorkCar(Car):
    def show_speed(self):
        print(f'Автомобиль {self.name}: ', end='')
        if self.speed > 40:
            print(f'превышает скорость!')
        print(f'Скорость = {self.speed} км\ч')


class SportCar(Car):
    pass


class PoliceCar(Car):
    is_police = True


my_towncar = TownCar(70, 'Зеленый', 'Жигуар', False)
my_workcar = WorkCar(30, 'Синий', 'datsun', False)
my_sportcar = SportCar(220, 'Красный', 'Ламбо', False)
my_policecar = PoliceCar(180, 'СпецЦвет', 'Шкода', True)

my_towncar.go()
my_towncar.turn('направо')
my_towncar.show_speed()
my_towncar.stop()

my_workcar.go()
my_workcar.turn('налево')
my_workcar.show_speed()
my_workcar.stop()

my_sportcar.go()
my_sportcar.turn('направо')
my_sportcar.show_speed()
my_sportcar.stop()

my_policecar.go()
my_policecar.turn('налево')
my_policecar.show_speed()
my_policecar.stop()
