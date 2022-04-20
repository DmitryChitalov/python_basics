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
    def __init__(self, speed, color, name, is_police=True):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return print(f'{self.name} begin drive')

    def stop(self):
        return print(f'{self.name} Car Stop')

    def turn(self):
        my_turn = input('Left or Right?: ')
        if my_turn == 'Left':
            print(f'{self.name} Turn left')
        elif my_turn == 'Right':
            print(f'{self.name} Car TURN RIGHT')
        else:
            print(f'{self.name} Car drive forward')

    def police(self):
        if self.is_police is True:
            print(f'Police CAR')
        else:
            print(f'{self.name} not police(')

    def show_speed(self):
        return print(f' Car Speed {self.speed()}')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Speed under limit 40, your speed {self.speed}')
        else:
            print(f'Just drive')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Speed under limit 60, your speed {self.speed}')
        else:
            print(f'Just drive')


class SportCar(Car):
    pass


class Police(Car):
    pass


wc = WorkCar(100, 'black', 'Lada', False)
wc.go(), wc.police(), wc.show_speed(), wc.turn(), wc.stop()
tc = TownCar(40, "red", 'reno', False)
tc.go(), tc.show_speed() , tc.stop()
sc = SportCar(222, 'blue', 'Kia', False)
p = Police(111, 'Special', 'BMW', True)
p.police(), p.show_speed()
