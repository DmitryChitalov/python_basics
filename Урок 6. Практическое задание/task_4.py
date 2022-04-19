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
    def __init__(self, color: str, name: str, is_police: bool):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self, speed):
        self.speed = speed
        print(f'Едем со скоростью {speed} км/ч')
    def stop(self):
        self.speed = 0
        print('Останавливаемся')
    def turn(self, direction: str):
        if self.speed > 0:
            print(f'Поворачиваем {direction}')
        else:
            print('Не можем повернуть - стоим')
    def show_speed(self):
        print(f'Скорость {self.speed} км/ч')
class TownCar(Car):
    def __init__(self, color: str, name: str):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False
    def show_speed(self):
        if self.speed > 60:
            print(f'Внимание! Превышение скорости - {self.speed} км/ч')
        else:
            print(f'Скорость {self.speed} км/ч')
class SportCar(Car):
    def __init__(self, color: str, name: str):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False
class WorkCar(Car):
    def __init__(self, color: str, name: str):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False
    def show_speed(self):
        if self.speed > 40:
            print(f'Внимание! Превышение скорости - {self.speed} км/ч')
        else:
            print(f'Скорость {self.speed} км/ч')
class PoliceCar(Car):
    def __init__(self, color: str, name: str):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = True
def bggg(bibika):
    print(f"{'Полицейский' if bibika.is_police else 'Гражданский'} автомобиль {bibika.name} - цвет {bibika.color}")
    bibika.go(40)
    bibika.show_speed()
    bibika.turn('направо')
    bibika.stop()
    bibika.show_speed()
    bibika.turn('налево')
    bibika.go(60)
    bibika.show_speed()
    bibika.go(120)
    bibika.show_speed()
    bibika.stop()
    print("Поездка окончена", end="\n\n")
ko = Car('металлик', 'Kia Optima', False)
bggg(ko)
vp = TownCar('красный', 'Volkswagen Polo')
bggg(vp)
bv = SportCar('черный', 'Bugatti Veyron')
bggg(bv)
ll = WorkCar('синий', 'Lada Largus')
bggg(ll)
fm = PoliceCar('розовый', 'Ford Mondeo')
bggg(fm)
