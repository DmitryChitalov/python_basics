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

    def __init__(self, speed, color, name, is_police, direction):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.direction = direction
        
    def go():
        print('The car has started')
    
    def stop():
        print('The car has stopped')
    
    def turn(self):
        print(f'The car has turned {self.direction}')
    
    def show_speed(self):
        print(f'The car speed is: {self.speed}')

class TownCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print('Over speed')
        else:
            return super().show_speed()

class SportCar(Car):

    def sport_method():
        print('This is sport car')

class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print('Over speed')
        else:
            return super().show_speed()

    
        
class PoliceCar(Car):

    def police_method():
        print('This is police car')

town_car = TownCar(speed=70, color='green', name='Golf', is_police=0, direction='right')
print(town_car.name)
print(town_car.speed)
town_car.show_speed()

# work_car = WorkCar(speed=40, color='green', name='Lada', is_police=0, direction='right')
work_car = WorkCar(40, 'green', 'Lada', 0, 'right')
print(work_car.name)
print(work_car.speed)
work_car.show_speed()