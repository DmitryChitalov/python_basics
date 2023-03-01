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
        return f'{self.name} поехали'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернула направо'

    def turn_left(self):
        return f'{self.name} повернула налево'

    def show_speed(self):
        return f'Текущая скорость авто {self.name} равна {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость городского авто {self.name} равна {self.speed}')

        if self.speed > 60:
            return f'Скорость {self.name} превышение скоростного режима городского авто'
        else:
            return f'Скорость {self.name} нормальная скорость для городского авто'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость городского авто {self.name} равна {self.speed}')

        if self.speed > 40:
            return f'Скорость {self.name} превышение скоростного режима городского авто'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} полицейский авто'
        else:
            return f'{self.name} не полицейский авто'


Ferrari = SportCar(250, 'Красный', 'Феррари', False)
Skoda = TownCar(55, 'Белая', 'Шкода', False)
Gazel = WorkCar(42, 'Синяя', 'Газель', False)
BMW = PoliceCar(140, 'Черная',  'БМВ', True)
print(Ferrari.turn_left())
print(f'Когда {Skoda.turn_right()}, {Ferrari.stop()}')
print(f'{Gazel.go()} со скоростью {Gazel.show_speed()}')
print(f'{Skoda.name} {Skoda.color}')
print(f'{Gazel.name} полицейская машина? {Gazel.is_police}')
print(f'{Ferrari.name} полицейская машина? {Ferrari.is_police}')
print(Gazel.show_speed())
print(Ferrari.show_speed())
print(BMW.police())
print(Skoda.show_speed())

