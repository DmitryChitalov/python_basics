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
class Car():
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False
    def show_speed(self):
        print(f'Скорость: {self.speed}')
    def go(self):
        print('Go...')
    def stop(self):
        print('Stop...')
    def turn(self, side):
        print(f'Turn {side}')

class SportCar(Car):
    def show_speed(self):
        return print('RB POOOWEEER!')

class TownCar(Car):
    def show_speed(self):
        if float(self.speed) > 60:
            return print('Превышение скорости')
        else:
            return print(f'Скорость - {self.speed}')
class WorkCar(Car):
    def show_speed(self):
        if float(self.speed) > 40:
            return print('Превышение скорости')
        else:
            return print(f'Скорость - {self.speed}')
class PoliceCar(Car):
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = True

sport_car = SportCar(100, 'White', 'Skyline R34')
sport_car.show_speed()

town_car = TownCar(70, 'Gray', 'Toyota BB')
town_car.show_speed()

work_car = WorkCar(50, 'Black', 'Lada')
work_car.turn('right')

police_car = PoliceCar(100, 'White/Blue', 'Skoda')
police_car.stop()

print(police_car.is_police)