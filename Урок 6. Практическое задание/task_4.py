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
# Подключаем модуль случайных чисел
from random import randrange

# Выводим название
print(f'\nЗадание 4.\n')

# Объявляем классы, материнский и дочерние
class Car:
    def __init__(self, speed: float, color: str, name: str, is_police=bool(False)):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed):
        self.speed = speed

    def stop(self):
        self.speed = 0
        print(f'{self.name} остановилась')

    def turn(self, direction):
        print(f'{self.name} повернула {direction}')

    def show_speed(self):
        print(f'{self.name} едет со скоростью {self.speed} км/ч')

    def __str__(self):
        return f'Скорость - {self.speed}\n' \
               f'Цвет - {self.color}\n' \
               f'Название - {self.name}\n'


class TownCar(Car):
    def show_speed(self):
        print(f'{self.name} едет со скоростью {self.speed} км/ч')
        if self.speed > 60:
            print(f'{self.name} превышает скорость на ', self.speed - 60)

class WorkCar(Car):
    def show_speed(self):
        print(f'{self.name} едет со скоростью {self.speed} км/ч')
        if self.speed > 40:
            print(f'{self.name} превышает скорость на ', self.speed - 40)

class SportCar(Car):
    def __init__(self, speed, color, name, is_police=bool(False)):
        super().__init__(speed, color, name, is_police)

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self.is_police = True

def __rand_turn():
    if randrange(2) == 0:
        return 'налево'
    else:
        return 'направо'

# Определяем переменные и выполняем методы класса
town_car = TownCar(randrange(90), 'белая', 'городская машина')
town_car.show_speed()
town_car.go(randrange(90))
town_car.show_speed()
town_car.stop()
town_car.turn(__rand_turn())
print(f'\n{town_car}')

sport_car = SportCar(randrange(180), 'красная', 'спортивная машина')
sport_car.show_speed()
sport_car.go(randrange(180))
sport_car.show_speed()
sport_car.stop()
sport_car.turn(__rand_turn())
print(f'\n{sport_car}')

work_car = WorkCar(randrange(90), 'желтая', 'служебная машина')
work_car.show_speed()
work_car.go(randrange(90))
work_car.show_speed()
work_car.stop()
work_car.turn(__rand_turn())
print(f'\n{work_car}')

police_car = PoliceCar(randrange(180), 'черная', 'полицейская машина', True)
police_car.show_speed()
police_car.go(randrange(180))
police_car.show_speed()
police_car.stop()
police_car.turn(__rand_turn())
print(f'\n{police_car}')
