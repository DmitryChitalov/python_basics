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

    # methods
    def go(self):
        return f'{self.name} движется'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} поворот на право'

    def turn_left(self):
        return f'{self.name} поворот на лево'

    def show_speed(self):
        return f'Скорость {self.name} составляет {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(
            f'Текущая скорость городского автомобиля {self.name} составляет {self.speed}')

        if self.speed > 60:
            return f'Скорость {self.name}  выше, чем допустимо для городского автомобиля'
        else:
            return f'У {self.name} допустимая скорость для городского автомобиля'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(
            f'Текущая скорость у рабочего автомобиля {self.name} составляет {self.speed}')

        if self.speed > 40:
            return f' Скорость {self.name} выше, чем допустимо для рабочего автомобиля'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} это полицейская машина'
        else:
            return f'{self.name} это не полицейская машина'


audi = SportCar(160, 'черный', 'Audi', False)
peugeot = TownCar(75, 'белый', 'Peugeot', False)
vw = WorkCar(30, 'синий', 'Volkswagen', False)
ford = PoliceCar(110, 'белый', 'Ford', True)
print(vw.turn_left())
print(f'{peugeot.turn_right()}, а {audi.stop()}')
print(f'{vw.go()} со скоростью {vw.show_speed()}')
print(f'{vw.name}  {vw.color}')
print(f' {audi.name} - полицейская машина? {audi.is_police}')
print(f' {vw.name}  - полицейская машина? {vw.is_police}')
print(audi.show_speed())
print(peugeot.show_speed())
print(ford.police())
print(ford.show_speed())
