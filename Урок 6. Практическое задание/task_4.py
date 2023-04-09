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

    def __init__(self, speed, color, brand, is_police):
        self.speed = speed
        self.color = color
        self.brand = brand
        self.is_police = is_police

    def go(self):
        print(f"Автомобиль {self.brand} начал движение")

    def stop(self):
        print(f"Автомобиль {self.brand} остановился")

    def turn(self, direction):
        print(f'Автомобиль {self.brand} повернул {direction}')

    def show_speed(self):
        print(f'Текущая скорость {self.brand}: {self.speed} км/ч')

    def police(self):
        if self.is_police:
            print(f'{self.brand} - полицейский автомобиль')
        else:
            print(f'{self.brand} - гражданский автомобиль')


class TownCar(Car):
    def __init__(self, speed, color, brand, is_police):
        super().__init__(speed, color, brand, is_police)

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Превышение скорости!')


class SportCar(Car):
    def __init__(self, speed, color, brand, is_police):
        super().__init__(speed, color, brand, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, brand, is_police):
        super().__init__(speed, color, brand, is_police)

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Превышение скорости!')


class PoliceCar(Car):
    def __init__(self, speed, color, brand, is_police):
        super().__init__(speed, color, brand, is_police)


tc = TownCar(61, 'red', 'Mazda', False)
sc = SportCar(120, 'yellow', 'Porshe', False)
wc = WorkCar(45, 'grey', 'VW', False)
pc = PoliceCar(100, 'blue', 'Ford', True)

tc.go()
sc.go()
wc.go()
pc.go()

tc.turn("направо")
sc.turn("налево")
wc.turn("обратно")
pc.turn("направо")

tc.show_speed()
sc.show_speed()
wc.show_speed()
pc.show_speed()

tc.police()
sc.police()
wc.police()
pc.police()

tc.stop()
sc.stop()
wc.stop()
pc.stop()
