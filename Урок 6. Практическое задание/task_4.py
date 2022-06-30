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
    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        return f'Машина {self.name} поехала'

    def stop(self):
        return f'Машина {self.name} остановилась'

    def turn(self, direction):
        return f'Машина {self.name} повернула' + direction

    def show_speed(self):
        return f'Текущая скорость {self.speed} км\ч'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'Превышение скорости! Ваша скорость {self.speed} км\ч'
        else:
            return f'Текущая скорость {self.speed}'


class SportCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed)


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'Превышение скорости! Ваша скорость {self.speed} км\ч'
        else:
            return f'Текущая скорость {self.speed}'


class PoliceCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed, True)


nissan = TownCar('Ниссан', 'Серый', 70)
police_car = PoliceCar('Тойота', 'Голубой', 100)
print(nissan.name, nissan.speed, nissan.is_police)
print(nissan.color, nissan.name, nissan.show_speed(), nissan.turn(direction=' на лево'))
print(police_car.name, police_car.color, police_car.show_speed(), police_car.is_police,
      police_car.turn(direction=' на право'))
