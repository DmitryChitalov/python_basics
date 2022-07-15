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


class Cars:
    name = None
    speed = None
    color = None
    is_police = False

    def __init__(self, name, speed, color, is_police = False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police
    def drive(self):
        return "Автомобиль поехал."
    def stop(self):
        return "Автомобиль остановился."
    def turn(self, direction):
        return "Автомобиль повернул на " + direction + "."
    def show_speed(self):
        return f'Текущая скорость автомобиля {self.name} {self.speed}.'

class TownCar(Cars):
    family = None
    def __init__(self, name, speed, color, family = True):
        super().__init__(name, speed, color)
        self.family = family
    def show_speed(self):
        print(f'Текущая скорость городского автомобиля {self.name} {self.speed}.')
        if self.speed > 60:
            return f'Скорость автомобиля {self.name} выше допустимой.'
        return f'Скорость автомобиля {self.name} в пределах допустимой.'

class SportCar(Cars):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color)

class WorkCar(Cars):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color)
    def show_speed(self):
        print(f'Текущая скорость рабочего автомобиля {self.name} {self.speed}.')
        if self.speed > 40:
            return f'Скорость автомобиля {self.name} выше допустимой.'
        return f'Скорость автомобиля {self.name} в пределах допустимой.'

class PoliceCar(Cars):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color, True)

ford = TownCar('Mercedes', 40, 'чёрный')
print(ford.name, ford.color, ford.speed, ford.is_police)
print(ford.drive(), ford.turn('лево'), ford.stop(), ford.show_speed())

sport = SportCar('Volkswagen', 120, 'красный')
print(sport.name, sport.color, sport.speed, sport.is_police)
print(sport.drive(), sport.turn('право'), sport.stop(), sport.show_speed())

work2 = WorkCar('КАМАЗ', 60, 'жёлтый')
print(work2.name, work2.color, work2.speed, work2.is_police)
print(work2.drive(), work2.turn('лево'), work2.stop(), work2.show_speed())

police = PoliceCar('Skoda', 80, 'белый')
print(police.name, police.color, police.speed, police.is_police)
print(police.drive(), police.turn('право'), police.stop(), police.show_speed())
