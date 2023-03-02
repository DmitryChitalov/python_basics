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
        if is_police:
            print(f'Создан полицейский автомобиль'
                  f' {self.name}, цвет {self.color}')
        else:
            print(f'Создан гражданский автомобиль'
                  f' {self.name}, цвет {self.color}')

    def go(self):
        return print(f'Машина {self.name} едет вперед'
                     f' со скоростью {self.speed}')

    def stop(self):
        self.speed = 0
        return print(f'Машина {self.name} остановилась. Скорость {self.speed}')

    def turn(self, dir):
        return print(f'Машина повернула {dir}')

    def show_speed(self):
        return print(f'Машина едет со скоростью {self.speed}')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class TownCar(Car):
    max_speed = 60

    def show_speed(self):
        if self.speed >= self.max_speed:
            return print(f'Превышение скорости на '
                         f'{self.speed - self.max_speed}')
        else:
            return print('Cкорость в допустимых пределах')


class WorkCar(Car):
    max_speed = 40

    def show_speed(self):
        if self.speed >= self.max_speed:
            return print(f'Превышение скорости на '
                         f'{self.speed - self.max_speed}')
        else:
            return print(f'Машина едет со скоростью {self.speed}')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


def drive(car):
    car.go()
    car.show_speed()
    car.turn('налево')
    car.go()
    car.show_speed()
    car.turn('направо')
    car.go()
    car.show_speed()
    car.stop()
    print('\n')


sport_car = SportCar(180, 'Red', 'Viper', False)
town_car = TownCar(80, 'Grey', 'Ford Focus', False)
work_car = WorkCar(50, 'Green', 'Transporter', False)
police_car = PoliceCar(130, 'White and Blue Lines', 'S300', True)

drive(sport_car)
drive(town_car)
drive(work_car)
drive(police_car)
