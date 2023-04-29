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
        print(f'{self.name} начинает движение.')

    def stop(self):
        print(f'{self.name} совершает остановку.')

    def turn(self, direction):
        print(f'{self.name} совершает поворот на{direction}')

    def show_speed(self):
        print(f'Текущая скорость {self.name} составляет {self.speed} км/ч')

    def get_car_info(self):
        print(f'Модель авто - {self.name}\n'
              f'Текущая скорость - {self.speed}\n'
              f'Цвет авто - {self.color}\n')
        if self.is_police:
            print(f'{self.name} является полицейским авто')
        if self.speed > 200:
            print(f'{self.name} является спортивным авто')


class TownCar(Car):
    def show_speed(self):
        max_speed = 60
        if self.speed > max_speed:
            print(f'Скорость автомобиля {self.name} превышает {max_speed} км/ч')
        else:
            print(f'Скорость автомобиля {self.name} составляет {self.speed} км/ч')


class WorkCar(Car):
    def show_speed(self):
        max_speed = 40
        if self.speed > max_speed:
            print(f'Скорость автомобиля {self.name} превышает {max_speed} км/ч')
        else:
            print(f'Скорость автомобиля {self.name} составляет {self.speed} км/ч')


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


obj_town_car = TownCar(55, 'Blue', 'Lada Granta', False)
obj_work_car = WorkCar(50, 'Yellow', 'Tesla Model X', False)
obj_sport_car = SportCar(220, 'Black', 'SportAuto', False)
obj_police_car = PoliceCar(150, 'Blue', 'Patriot', True)

print(obj_police_car.name, obj_police_car.speed, obj_police_car.color, obj_police_car.is_police)
obj_work_car.go()
obj_work_car.turn('лево')
obj_work_car.stop()
obj_sport_car.get_car_info()
