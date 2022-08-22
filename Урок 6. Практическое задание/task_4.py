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

    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'\n{self.name} Поехала'

    def stop(self):
        return f'\n{self.name} Остановилась'

    def turn(self, direction):
        return f'\n{self.name} Повернула {direction}'

    def show_speed(self):
        return f'\n{self.speed} - Текущая скорость'


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            return f'\nСкорость {self.speed} выше положенной'
        else:
            return f'\nСкорость {self.speed}  в норме'


class SportCar(Car):
    pass

class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            return f'\nСкорость {self.speed} выше положенной'
        else:
            return f'\nСкорость {self.speed}  в норме'

class PoliceCar(Car):
    pass




a = TownCar(66, 'красная', 'Tesla', True)
print(a.go(), a.turn('налево'), a.show_speed(), a.stop())

a = WorkCar(36, 'синяя', 'Vesta', True)
print(a.go(), a.turn('налево'), a.show_speed(), a.stop())

a = SportCar(236, 'черная', 'Гранта', False)
print(a.go(), a.turn('в стену'), a.show_speed(), a.stop())

a = PoliceCar(29, ',белая', 'Буханка', False)
print(a.go(), a.turn('налево'), a.turn('направо'), a.turn('назад'), a.show_speed(), a.stop())