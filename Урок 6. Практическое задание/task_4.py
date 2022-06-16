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

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def show_speed(self):
        print(f'Скорость: {self.speed}')

    @staticmethod
    def go():
        print('Машина поехала')

    @staticmethod
    def stop():
        print('Машина остановилась')

    @staticmethod
    def turn(direction):
        print(f'Машина повернула на {direction}')


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


class TownCar(Car):
    def show_speed(self):
        return print('Превышение скорости') if float(self.speed) > 60 else print(f'Скорость - {self.speed}')


class WorkCar(Car):
    def show_speed(self):
        return print('Превышение скорости') if float(self.speed) > 40 else print(f'Скорость - {self.speed}')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = True


town_car = TownCar(80, 'Белый', 'Toyota Avensis')
town_car.show_speed()

work_car = WorkCar(60, 'Синий', 'Reno Clio')
work_car.turn('лево')

sport_car = SportCar(120, 'Чёрный', 'Mitsubishi')
sport_car.show_speed()

police_car = PoliceCar(100, 'Белый', 'Volvo')
police_car.stop()

print(police_car.is_police)
