# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.

class Car:

    def __init__(self, max_speed, speed, color, name, is_police):
        self.max_speed = max_speed
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f'Новый автомобиль {name},  {color} цвет')

    def show_speed(self, speed):
        self.speed = speed
        print(f'Скорость движения {self.speed} км/ч')

    def go(self):
        print(f'{self.name} начала движение')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self, direction):
        print(f'{self.name} повернула {direction}')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        self.max_speed = 60
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f'Это семейный автомобиль')

    def show_speed(self, speed):
        self.speed = speed
        print(f'Скорость движения {self.speed} км/ч')
        if self.speed > self.max_speed and not self.is_police:
            print('Превышение допустимой скорости!')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        self.max_speed = speed
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f'Это спортивный автомобиль')


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        self.max_speed = 40
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f'Это служебный автомобиль')

    def show_speed(self, speed):
        self.speed = speed
        print(f'Скорость движения {self.speed} км/ч')
        if self.speed > self.max_speed and not self.is_police:
            print('Превышение допустимой скорости!')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        self.max_speed = speed
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f'Это полицейский автомобиль')


TownCar_ = TownCar(60, 'черный', 'Honda', False)
TownCar_.go()
TownCar_.show_speed(40)
TownCar_.show_speed(80)
TownCar_.turn('направо')
TownCar_.stop()
print()

work_car = WorkCar(60, 'серый', 'Волга', False)
work_car.go()
work_car.show_speed(40)
work_car.show_speed(90)
work_car.show_speed(60)
work_car.show_speed(40)
work_car.stop()
print()

police_car = PoliceCar(0, 'белый', 'Toyota', True)
police_car.go()
police_car.show_speed(80)
police_car.turn('налево')
police_car.turn('направо')
police_car.stop()
print()

sport_car = SportCar(60, 'черный', 'Nissan', False)
sport_car.go()
sport_car.show_speed(60)
sport_car.show_speed(70)
sport_car.stop()
print()