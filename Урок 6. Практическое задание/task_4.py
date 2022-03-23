"""
Задание 4.

Реализуйте базовый класс Car. У данного класса должны быть следующие
публичные атрибуты:
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

    def go(self):
        return f'The {self.name} is start.'

    def stop(self):
        return f'The {self.name} is stop.'

    def turn(self, direction):
        return f'The {self.name} turned to {direction}'

    def show_speed(self):
        return f'Your speed is {self.speed}'


class TownCar(Car):
    def show_speed(self):
        # def __init__(self, speed, color, name, is_police):
        #     super().__init__(speed, color, name, is_police)
        if self.speed > 60:
            return f'Your speed is too high! Your speed is {self.speed}'
        else:
            return f"{self.name}'s is normal"


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'Your speed is too high! Your speed is {self.speed}'
        else:
            return f"{self.name}'s is normal"


class PoliceCar(Car):
    pass


town = TownCar('Kia', 70, 'black', False)
print('TownCar:' + town.go(), town.show_speed(), town.turn('left'),
      town.stop())

sport = SportCar('Nissan', 210, 'blue', False)
print('SportCar:' + sport.go(), sport.show_speed(), sport.turn('left'),
      sport.stop())

work = WorkCar('Forklift', 30, 'yellow', False)
print('WorkCar:' + work.go(), work.show_speed(), work.turn('right'),
      work.stop())

police = PoliceCar('Skoda', 100, 'white', True)
print('PoliceCar:' + police.go(), police.show_speed(), police.turn('right'),
      police.stop())
