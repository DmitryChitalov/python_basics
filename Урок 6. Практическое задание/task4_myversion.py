"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните
вызов методов и также покажите результат
"""


class Car:
    # атрибуты родительского класса
    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    # методы родительского класса
    def go(self):
        return f'Ваша машина {self.name} поехала.'

    def stop(self):
        return f'\n Ваша машина {self.name} остановилась.'

    def turn(self, direction):
        return f'\n Ваша машина {self.name} певернула {direction}'

    def show_speed(self):
        return f'\n Ваша скорость сейчас: {self.speed}'


class TownCar(Car):
    # метод дочернего класса
    def show_speed(self):
        if self.speed > 60:
            return f'\n Внимание! Ваша скорость {self.speed} км/ч превышает норму, сбавьте её!'
        else:
            return f'\n Ваша скорость {self.speed} в норме'


class SportCar(Car):
    pass


class WorkCar(Car):
    # метод дочернего класса
    def show_speed(self):
        if self.speed > 40:
            return f'\n Внимание! Ваша скорость {self.speed} км/ч превышает норму, сбавьте её!'
        else:
            return f'\n Ваша скорость {self.speed} в норме'


class PoliceCar(Car):
    pass


town = TownCar('Genesis GV80', 80, 'black', False)
print('1: \n' + town.go(), town.show_speed(), town.turn('налево'), town.turn('направо'), town.stop())

sport = SportCar('Bugatti Veyron', 170, 'red', False)
print('2: \n' + sport.go(), sport.show_speed(), sport.turn('нелево'), sport.stop())

work = WorkCar('Тонар-7502', 40, 'orange', False)
print('3: \n' + work.go(), work.show_speed(), work.turn('направо'), work.stop())

police = PoliceCar('UAZ Hunter', 60, 'white', False)
print('4: \n' + police.go(), police.show_speed(), police.turn('направо'), police.turn('налево'), police.stop())
