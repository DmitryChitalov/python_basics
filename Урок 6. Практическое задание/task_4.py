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
    def __init__(self, color, name, is_police):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed):
        self.speed = speed
        print(f'Машина тронулась со скоростью {self.speed} км/ч')

    def stop(self):
        self.speed = 0
        print(f'Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(f'Машина развила скорость {self.speed} км/ч')

    def __str__(self):
        return f'{self.name} ({self.color})' + (' - полицейский' if self.is_police else '')

class TownCar(Car):

    def __init__(self, color, name):
        super().__init__(color, name, False)

    def show_speed(self):
        super().show_speed()
        if (self.speed > 60):
            print(f'Скорость превысила допустимую')
    
class SportCar(Car):

    def __init__(self, color, name):
        super().__init__(color, name, False)
    
class WorkCar(Car):

    def __init__(self, color, name):
        super().__init__(color, name, False)

    def show_speed(self):
        super().show_speed()
        if (self.speed > 40):
            print(f'Скорость превысила допустимую')
    
class PoliceCar(Car):

    def __init__(self, color, name):
        super().__init__(color, name, True)

car = WorkCar('Белый', 'Nissan Qashqai')
print(car)
car.go(20)
car.turn('на лево')
car.speed = 60
car.show_speed()
car.stop()
car.show_speed()
print('')
car = PoliceCar('Черный', 'BMW')
print(car)
car.go(200)
car.show_speed()
