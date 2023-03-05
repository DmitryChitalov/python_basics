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
        return f'Машина {self.name} поехала'

    def stop(self):
        return f'Машина {self.name} остановилось'

    def turn(self, direction):
        return f'Машина {self.name} повернула на {direction}'

    def show_speed(self):
        return f'Скорость {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return 'Превышение скорости'
        else:
            return Car.show_speed(self)


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return 'Превышение скорости'
        else:
            return Car.show_speed(self)


class PoliceCar(Car):
    pass


town_car = TownCar(70, 'белый', 'бетонамешалка', False)
print(town_car.go())
print(town_car.stop())
print(town_car.turn('лево'))
print(town_car.show_speed())

sport_car = SportCar(180, 'Красный', 'ферари', False)
print(sport_car.go())
print(sport_car.stop())
print(sport_car.turn('лево'))
print(sport_car.show_speed())

work_car = WorkCar(30, 'серый', 'газ', False)
print(work_car.go())
print(work_car.stop())
print(work_car.turn('право'))
print(work_car.show_speed())

police_car = PoliceCar(120, 'белый', 'приора', True)
print(police_car.go())
print(police_car.stop())
print(police_car.turn('лево'))
print(police_car.show_speed())
