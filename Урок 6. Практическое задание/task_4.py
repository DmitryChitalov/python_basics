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
    def __init__(self, speed, color, name, is_police=True):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Автомобиль поехал')

    def stop(self):
        print('Автомобиль остановился')

    def turn(self, direction):
        self.direction = direction
        if direction == 'right':
            print('Автомобиль повернул направо')
        elif direction == 'left':
            print('Автомобиль повернул налево')
        else:
            print('Автомобиль продолжает ехать прямо')

    def show_speed(self):
        print(f'Текущая скорость автомобиля - {self.speed} км/ч')


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f'Скорость превышена!'
                  f'Текущая скорость автомобиля - {self.speed} км/ч')
        else:
            print(f'Текущая скорость автомобиля - {self.speed} км/ч')


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print(f'Скорость превышена!'
                  f'Текущая скорость автомобиля - {self.speed} км/ч')
        else:
            print(f'Текущая скорость автомобиля - {self.speed} км/ч')


class PoliceCar(Car):
    pass


a = Car(60, 'red', 'BMW', True)
print(a.name)
print(a.speed)
print(a.color)
print(a.is_police)
a.go()
a.stop()
a.turn('right')
a.show_speed()

b = TownCar(70, 'pink', 'Audi', False)
print(b.is_police)
b.show_speed()

c = WorkCar(41, 'yellow', 'Daewoo')
print(c.color)
c.show_speed()
