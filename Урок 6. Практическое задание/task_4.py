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
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'\n Автомобиль {self.name} едет со скоростью {self.speed} км/ч')

    def stop(self):
        print(f'\n Автомобиль {self.name} остановился')

    def turn(self, direction):
        print(f'\n Автомобиль {self.name} повернул {direction}')

    def show_speed(self):
        print(f'\n Скорость автомобиля {self.name}: {self.speed} км/ч')

    def show_parameters(self):
        print(f'\n Марка автомобиля: {self.name}')
        print(f'\n Цвет автомобиля: {self.color}')
        if self.is_police:
            print('\n Автомобиль является полицейским')
        else:
            print('\n Автомобиль гражданский')


class TownCar(Car):
    speed_limit = 60

    def show_speed(self):
        if self.speed > self.speed_limit:
            print(f'\n Допустимая скорость {self.speed_limit} км/ч'
                  f'\n Ваша скорость равна {self.speed} км/ч'
                  f'\n Вы двигаетесь с превышением скорости на {self.speed - self.speed_limit} км/ч')
        else:
            print(f'\n Допустимая скорость {self.speed_limit} км/ч')
            print(f'\n Ваша скорость равна {self.speed} км/ч')


class SportCar(Car):
    speed_limit = 200


class WorkCar(Car):
    speed_limit = 40

    def show_speed(self):
        if self.speed > self.speed_limit:
            print(f'\n Допустимая скорость {self.speed_limit} км/ч'
                  f'\n Ваша скорость равна {self.speed} км/ч'
                  f'\n Вы двигаетесь с превышением скорости равным {self.speed - self.speed_limit} км/ч')
        else:
            print(f'\n Допустимая скорость {self.speed_limit} км/ч'
                  f'\n Ваша скорость равна {self.speed} км/ч')


class PoliceCar(Car):
    speed_limit = 200

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self.is_police = True


new_car = TownCar(75, 'red', 'Audi', False)
new_car.show_parameters()
new_car.go()
new_car.show_speed()
new_car.turn('налево')
new_car.stop()

new_car2 = WorkCar(40, 'black', 'Ford', False)
new_car2.show_parameters()
new_car2.go()
new_car2.turn('налево')
new_car2.show_speed()
new_car2.stop()

new_car3 = PoliceCar(80, 'white-blue', 'Dodge', False)
new_car3.show_parameters()
