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

    def __init__(self, name, speed, color, is_police=True):
        self.name = name
        self.speed = speed
        self.color = color
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
            return f'Скорость машины {self.name}, Вы не привышаете допустимую скорость'


class SportCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\nСкорость выше допустимой! Скорость равна {self.speed}'
        else:
            return f'Скорость машины {self.name}, Вы не привышаете допустимую скорость'


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nСкорость выше допустимой! Скорость равна {self.speed}'
        else:
            return f'Скорость машины {self.name}, Вы не привышаете допустимую скорость'


class PoliceCar(Car):
    pass


town = TownCar('BMW X3', 90, 'Красная', False)
print('Машина 1:\n' + town.go(), town.show_speed(), town.turn('лево'), town.turn('право'), town.stop())

sport = SportCar('Lamborghini aventador', 170, 'Желтая', False)
print('Машина 2:\n' + sport.go(), sport.show_speed(), sport.turn('право'), sport.stop())

work = WorkCar('Лада Granta', 30, 'Синия', False)
print('Машина 3:\n' + work.go(), work.show_speed(), work.turn('лево'), work.stop())

police = PoliceCar('УАЗ Patriot', 40, 'Синия', True)
print('Машина 4:\n' + work.go(), work.show_speed(), work.turn('лево'), work.stop())
