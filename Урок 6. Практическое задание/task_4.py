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
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} движется')

    def stop(self):
        print(f'Машина {self.name} стоит')

    def turn(self, direction):
        print(f'Машина {self.name} поворачивает {direction}')

    def show_speed(self):
        print(f'Текущая скорость {self.name}: {self.speed} км/ч.')

    def police(self):
        if self.is_police:
            print(f'{self.name} Полицейский автомобиль')
        else:
            print(f'{self.name} Не полицейский автомобиль')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name} вы превышаете скорость!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'{self.name} вы превышаете скорость!')


class PoliceCar(Car):
    pass


first_car = TownCar(50, "черной", "Toyota", False)
second_car = SportCar(220, "желтой", "Lamborghini", False)
third_car = WorkCar(50, "синей", "Nissan", False)
fourth_car = PoliceCar(90, "белой", "Skoda", True)

print(f'Скорость {first_car.color} {first_car.name} {first_car.speed} км/ч.')
print(f'Скорость {second_car.color} {second_car.name} {second_car.speed} км/ч.')
print(f'Скорость {third_car.color} {third_car.name} {third_car.speed} км/ч.')
print(f'Скорость {fourth_car.color} {fourth_car.name} {fourth_car.speed} км/ч.')

first_car.show_speed()
second_car.show_speed()
third_car.show_speed()
fourth_car.show_speed()

first_car.go()
second_car.stop()
third_car.turn('влево')
fourth_car.police()
