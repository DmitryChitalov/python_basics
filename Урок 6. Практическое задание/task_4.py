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
    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def gou(self):
        return f'{self.color} {self.name} едет'

    def stop(self):
        return f'{self.color} {self.name} остановился'

    def turn(self, direction):
        return f'{self.color} {self.name} поворачивает {direction}'

    def show_speed(self):
        return f'скорость {self.name} = {self.speed} км/ч'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'городской {self.name} превысил скорость на {self.speed - 60} км/ч'
        else:
            return f'скорость {self.name} =  {self.speed} км/ч'


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'служебный {self.name} превысил скорость на {self.speed - 40} км/ч'
        else:
            return f'скорость {self.name} =  {self.speed} км/ч'


class SportCar(Car):
    pass


class PoliceCar(Car):
    def police(self):
        if self.is_police:
            return f'{self.name} - это полиция!'


print("\n")
t_car = TownCar(60, 'синий', 'Renault Logan', False)
print(t_car.gou())
print(t_car.show_speed())
t_car.speed = 80
print(t_car.show_speed())
print(t_car.turn('направо'))
print(t_car.stop())
print("\n")
w_car = WorkCar(30, 'чёрный', 'УАЗ Патриот', False)
print(w_car.gou())
print(w_car.show_speed())
w_car.speed = 50
print(w_car.show_speed())
print(w_car.turn('налево'))
print(w_car.gou())
print(w_car.stop())
print("\n")
p_car = PoliceCar(0, 'белый', 'Toyota Crown Victoria', True)
print(p_car.show_speed())
print(p_car.police())
print("\n")
s_car = SportCar(60, 'жёлтый', 'Chevrolet Camaro', False)
print(s_car.gou())
print(s_car.show_speed())
s_car.speed = 150
print(s_car.show_speed())
