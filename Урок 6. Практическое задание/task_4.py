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

    def go(self):
        return f'Машина {self.name} поехала.'

    def stop(self):
        return f'\nМашина {self.name} остановилась.'

    def turn(self, direction):
        return f'\nМашина {self.name} повернула в {direction}'

    def show_speed(self):
        return f'\nВаша скорость {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\nВаша скорость превышена и составляет {self.speed}'
        else:
            return f'Скорость машины {self.name} нормальная'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nВаша скорость превышена и составляет {self.speed}'
        else:
            return f'Скорость машины {self.name} нормальная'


class PoliceCar(Car):
    pass


town = TownCar('Жигули', 70, 'черная', False)
print('1:\n' + town.go(), town.show_speed(), town.turn('влево'), town.turn('вправо'), town.stop())

sport = SportCar('Нива', 170, '', False)
print('2:\n' + sport.go(), sport.show_speed(), sport.turn('вправо'), sport.stop())

work = WorkCar('Камаз', 30, 'красный', False)
print('3:\n' + work.go(), work.show_speed(), work.turn('влево'), work.stop())

police = PoliceCar('Москвич', 100, 'зеленый', True)
print('4:\n' + police.go(), police.show_speed(), police.turn('влево'), police.stop())
