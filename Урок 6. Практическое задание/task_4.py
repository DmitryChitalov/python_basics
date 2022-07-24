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
    def __init__(self, color, name, speed, is_police=True):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.color} машина {self.name} начала движение.'

    def stop(self):
        return f'\nМашина {self.name} остановилась.'

    def turn(self, direction):
        return f'\nМашина {self.name} повернула на {direction}'

    def show_speed(self):
        return f'\nВаша скорость {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\nСкорость выше допустимой! Скорость равна {self.speed}'
        else:
            return f'\nВы не привышаете допустимую скорость! Скорость равно {self.speed}'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nСкорость выше допустимой! Скорость равна {self.speed}'
        else:
            return f'\nВы не привышаете допустимую скорость! Скорость равно {self.speed}'


class PoliceCar(Car):
    def __init__(self, color, name, is_sherif):
        self.is_sherif = is_sherif
        super().__init__(color, name, str('не важна т.к. вы полицейский'), True)


town = TownCar('Красная', 'BMW', 70, False)
print('Машина 1:\n' + town.go(), town.show_speed(), town.turn('лево'), town.turn('право'), town.stop())

sport = SportCar('белая', 'Mercedes', 120, False)
print('Машина 2:\n' + sport.go(), sport.show_speed(), sport.turn('право'), sport.stop())

work = WorkCar('Зеленая', 'Chevrolet', 35, False)
print('Машина 3:\n' + work.go(), work.show_speed(), work.turn('право'), work.stop())

police = PoliceCar('Синия', 'Jelly', True)
print('Машина 4:\n' + police.go(), police.show_speed(), police.turn('право'), police.stop())
