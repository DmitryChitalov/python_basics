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
        print('{} поехала!'.format(self.name))

    def stop(self):
        print('{} остановилась!'.format(self.name))

    def turn(self, direction):
        print('{} повернула {}!'.format(self.name, direction))

    def show_speed(self):
        print('Текущая скорость: ', self.speed)


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Внимание! Вы превысили скорость.')

class SportsCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        print('Текущая скорость: ', self.speed)
        if self.speed > 40:
            print('Внимание! Вы превысили скорость')


class PoliceCar(Car):
    pass

sports_car = SportsCar(240, 'Красная', 'Спортивная машина', False)
town_car = TownCar(140, 'Серая', 'Городская машина', False)
work_car = WorkCar(90, 'Жёлтая', 'Рабочая машина', False)
police_car = PoliceCar(210, 'Чёрная', 'Полицейская машина', True)

sports_car.show_speed()
print()
print(town_car.name)
print()
work_car.show_speed()
print(work_car.name, work_car.color)
print()
police_car.show_speed()
sports_car.turn('направо')
