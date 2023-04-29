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

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self, speed):
        self.speed = speed
        return f'Машина {self.name} поехала.'

    def stop(self):
        self.speed = 0
        return f'Машина {self.name} остановилась.'

    def turn(self, direction):
        if direction == "лево" or direction == "право":
            return f'Машина {self.name} повернула на {direction}'
        else:
            return f'Могу повернуть только на "лево" или на "право"'

    def show_speed(self):
        return f'Текущая скорость автомобиля: {self.speed}'


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            return f'Вы превысили скорость!'
        else:
            return f'Текущая скорость автомобиля: {self.speed}'


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'Вы превысили скорость!'
        else:
            return f'Текущая скорость автомобиля: {self.speed}'


town_car = TownCar('Жигули', 0, 'синий')
print(town_car.go(10))
print(town_car.show_speed())
print(town_car.go(50))
print(town_car.show_speed())
print(town_car.turn("лево"))
print(town_car.turn("право"))
print(town_car.turn("назад"))
print(town_car.show_speed())
print(town_car.go(65))
print(town_car.show_speed())
print(town_car.stop())
print(town_car.show_speed())

print()

work_car = WorkCar('Волга', 0, 'белый', True)
print(work_car.go(10))
print(work_car.show_speed())
print(work_car.go(50))
print(work_car.show_speed())
print(work_car.go(40))
print(work_car.show_speed())
print(work_car.turn("лево"))
print(work_car.turn("право"))
print(work_car.turn("назад"))
print(work_car.show_speed())
print(work_car.stop())
print(work_car.show_speed())
