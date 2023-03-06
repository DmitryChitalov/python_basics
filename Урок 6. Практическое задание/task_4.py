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


class Car:
    def __init__(self, color, name):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False
        self.state = 'Stopped'

    def go(self):
        self.state = 'Moving'
        self.speed = random.randint(1, 100)
        return f'{self.state}, скорость - {self.speed}, машина поехала'

    def stop(self):
        self.state = 'Stopped'
        self.speed = 0
        return f'{self.state}, скорость - 0, машина остановилась'

    def left(self):
        self.state = 'Moving'
        self.speed = random.randint(1, 100)
        return f'{self.state}, скорость - {self.speed}, машина повернула налево'

    def right(self):
        self.state = 'Moving'
        self.speed = random.randint(1, 100)
        return f'{self.state}, скорость - {self.speed}, машина повернула направо'

    def show_speed(self):
        return self.speed


class TownCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name)

    def show_speed(self):
        if self.speed > 60:
            return f'Ваша скорость {self.speed}, нужно ехать медленнее'
        else:
            return self.speed


class SportCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name)


class WorkCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name)

    def show_speed(self):
        if self.speed > 40:
            return f'Ваша скорость {self.speed}, нужно ехать медленнее'
        else:
            return self.speed


class PoliceCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name)
        self.is_police = True


my_car = Car('Black', 'Moskvich')
print('Моя скорость', my_car.speed)
print('Моё состояние', my_car.state)
print('Мой цвет', my_car.color)
print(my_car.go())
print('Моя скорость', my_car.speed)
print('Полицейска машина - ', my_car.is_police)
print(my_car.left())
print('Моя скорость', my_car.show_speed())

print('\n')

my_car = TownCar('White', 'Nissan')
print('Моя скорость', my_car.speed)
print('Моё состояние', my_car.state)
print('Мой цвет', my_car.color)
print(my_car.go())
print('Моя скорость', my_car.speed)
print('Полицейска машина - ', my_car.is_police)
print(my_car.left())
print('Моя скорость', my_car.show_speed())

print('\n')

my_car = SportCar('Red', 'Ferrari')
print('Моя скорость', my_car.speed)
print('Моё состояние', my_car.state)
print('Мой цвет', my_car.color)
print(my_car.go())
print('Моя скорость', my_car.speed)
print('Полицейска машина - ', my_car.is_police)
print(my_car.left())
print('Моя скорость', my_car.show_speed())

print('\n')

my_car = WorkCar('Yellow', 'CAT')
print('Моя скорость', my_car.speed)
print('Моё состояние', my_car.state)
print('Мой цвет', my_car.color)
print(my_car.go())
print('Моя скорость', my_car.speed)
print('Полицейска машина - ', my_car.is_police)
print(my_car.left())
print('Моя скорость', my_car.show_speed())

print('\n')

my_car = PoliceCar('Blue', 'Peugeot')
print('Моя скорость', my_car.speed)
print('Моё состояние', my_car.state)
print('Мой цвет', my_car.color)
print(my_car.go())
print('Моя скорость', my_car.speed)
print('Полицейска машина - ', my_car.is_police)
print(my_car.left())
print('Моя скорость', my_car.show_speed())
