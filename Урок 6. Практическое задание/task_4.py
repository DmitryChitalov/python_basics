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
        print('Едет')

    def stop(self):
        print('Стоит')

    def turn(self, direction):
        print('Повернула на', direction)

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def show_speed(self):
        if (self.speed > 60):
            print(f'Превышении скорости на {self.speed - 60}')


class SportCar(Car):
    def __str__(self):
        return f"{self.speed}, {self.color}, {self.name}, {self.is_police}"


class WorkCar(Car):
    def show_speed(self):
        if (self.speed > 40):
            print(f'Превышении скорости на {self.speed - 40}')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


town_car = TownCar(67, 'green', 'bus', False)
town_car.show_speed()
town_car.stop()

sport_car = SportCar(187, 'red', 'Ferrari', False)
sport_car.turn('лево')
print(str(sport_car))

work_car = WorkCar(43, 'black', 'Honda', False)
work_car.show_speed()

police_car = PoliceCar(74, 'white', 'BMW', True)
police_car.go()
