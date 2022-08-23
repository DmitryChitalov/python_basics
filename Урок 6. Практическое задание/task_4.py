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

"""
Выполенине! Емельяненко А.А.
"""


class Car:

    def __init__(self, name, speed, color, is_formula=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_formula = is_formula

    def go(self):
        return f'То {self.name} старт.'

    def stop(self):
        return f'\nТо {self.name} стоп.'

    def turn(self, direction):
        return f'\nТо {self.name} свернуть {direction}'

    def show_speed(self):
        return f'\nВаша скорость равна {self.speed}'


class FormulaCar(Car):
    def show_speed(self):
        if self.speed > 320:
            return f'\nВаша скорость выше допустимой! Ваша скорость равна {self.speed}'
        else:
            return f'Скорость {self.name} это нормальная'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 90:
            return f'\nВаша скорость выше допустимой! Ваша скорость равна {self.speed}'
        else:
            return f'Скорость {self.name} это нормальная'


class FiatCar(Car):
    pass


town = FormulaCar('Formula', 190, 'blue', False)
print('1:\n' + town.go(), town.show_speed(), town.turn('left'), town.turn('right'), town.stop())

sport = SportCar('Mitsubishi', 150, 'red', False)
print('2:\n' + sport.go(), sport.show_speed(), sport.turn('left'), sport.stop())

work = FiatCar('Fiat', 60, 'black', False)
print('3:\n' + work.go(), work.show_speed(), work.turn('right'), work.stop())
