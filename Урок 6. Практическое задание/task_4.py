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
    def __init__(self, name, color, speed, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed):
        self.speed = speed
        print(f'{self.name} цвет {self.color} двигается со скоростью {self.speed} км/ч')
    def stop(self):
        self.speed = 0
        print(f'{self.name} цвет {self.color} прекратила движение')

    def turn(self, direction):
        self.direction = direction
        print(f'{self.name} цвет {self.color} повернула {self.direction}')

    def show_speed(self):
        print(f'Скорость {self.name} цвет {self.color} равна {self.speed}')

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name} цвет {self.color} превысила ограничение скорости (60 км/ч)')
        else:
            print(f'Скорость {self.name} цвет {self.color} = {self.speed} км/ч')

class SportCar(Car):
    pass
class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'{self.name} цвет {self.color} превысила ограничение скорости (40 км/ч)')
        else:
            print(f'Скорость {self.name} цвет {self.color} = {self.speed} км/ч')

class PoliceCar(Car):
    def __init__(self, name, color, speed):
        Car.__init__(self, name, color, speed, is_police=True)


town_car = TownCar("BMW", "черный", 0)
print(town_car.name)
print(f'{town_car.name} полицейский: {"да" if town_car.is_police else "нет"}')
town_car.show_speed()
town_car.go(88)
town_car.show_speed()
town_car.turn("налево")
town_car.stop()


print("\n")

work_car = WorkCar("Газель", "желтый", 0)
print(work_car.name)
print(f'{work_car.name} полицейский: {"да" if work_car.is_police else "нет"}')
work_car.show_speed()
work_car.go(78)
work_car.show_speed()
work_car.turn("направо")
work_car.go(22)
work_car.show_speed()
work_car.turn("налево")


print("\n")

sport_car = SportCar("Lamborgini", "красный", 0)
print(sport_car.name)
print(f'{sport_car.name} полицейский: {"да" if sport_car.is_police else "нет"}')
sport_car.go(120)
sport_car.stop()
sport_car.go(185)


print("\n")

police_car = PoliceCar("УАЗ", "бело-синий", 0)
print(police_car.name)
print(f'{police_car.name} полицейский: {"да" if police_car.is_police else "нет"}')
police_car.go(80)
police_car.stop()
police_car.show_speed()
police_car.go(125)
