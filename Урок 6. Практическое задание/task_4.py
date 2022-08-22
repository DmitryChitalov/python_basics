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
        print('Автомобиль поехал')

    def stop(self):
        print('Автомобиль остановился')

    def turn(self, direction):
        self.direction = direction
        if direction == 'right':
            print('Автомобиль повернул направо')
        elif direction == 'left':
            print('Автомобиль повернул налево')
        else:
            print('Автомобиль продолжает ехать прямо')

    def show_speed(self):
        print(f'Текущая скорость автомобиля - {self.speed} км/ч')


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f'Скорость превышена!'
                  f'Текущая скорость автомобиля - {self.speed} км/ч')
        else:
            print(f'Текущая скорость автомобиля - {self.speed} км/ч')


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print(f'Скорость превышена!'
                  f'Текущая скорость автомобиля - {self.speed} км/ч')
        else:
            print(f'Текущая скорость автомобиля - {self.speed} км/ч')


class PoliceCar(Car):
    pass


car_1 = Car(150, 'пурпурный', 'BMW', True)
print(car_1.name)
print(car_1.speed)
print(car_1.color)
print(car_1.is_police)
car_1.go()
car_1.stop()
car_1.turn('right')
car_1.show_speed()

car_2 = TownCar(71, 'красный', 'LADA', False)
print(car_2.is_police)
car_2.show_speed()

car_3 = WorkCar(44, 'желтый', 'KIA')
print(car_3.color)
car_3.show_speed()
