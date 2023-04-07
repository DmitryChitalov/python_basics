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
from random import randint


class Car:
    def __init__(self, in_speed, in_color, in_name, in_is_police):
        self.speed = in_speed
        self.color = in_color
        self.name = in_name
        self.is_police = in_is_police

    def go(self):
        print(f"Машина {self.name} поехала")

    def stop(self):
        print(f"Машина {self.name} остановилась")

    def turn(self, direction):
        print(f"Машина {self.name} повернула {direction}")

    def show_speed(self):
        print(f"Текущая скорость {self.name} (метод родительского класса): {self.speed}")


class TownCar(Car):
    def __init__(self, in_speed, in_color, in_name, in_is_police=False):
        super().__init__(in_speed, in_color, in_name, in_is_police)

    def show_speed(self):
        if self.speed >= 60:
            print(f"Допущено превышение скорости (>60 км/ч): {self.speed}")
        else:
            print(f"Текущая скорость {self.name} (метод класса TownCar): {self.speed}")


class SportCar(Car):
    def __init__(self, in_speed, in_color, in_name, in_is_police=False):
        super().__init__(in_speed, in_color, in_name, in_is_police)


class WorkCar(Car):
    def __init__(self, in_speed, in_color, in_name, in_is_police=False):
        super().__init__(in_speed, in_color, in_name, in_is_police)

    def show_speed(self):
        if self.speed >= 40:
            print(f"Допущено превышение скорости (>40 км/ч): {self.speed}")
        else:
            print(f"Текущая скорость {self.name} (метод класса WorkCar): {self.speed}")


class PoliceCar(Car):
    def __init__(self, in_speed, in_color, in_name, in_is_police=True):
        super().__init__(in_speed, in_color, in_name, in_is_police)


# инициализация объектов и их атрибутов
obj_town_car = TownCar(65, "красная", "Lincoln TownCar")
obj_sport_car = SportCar(180, "синяя", "Chevrolet Camaro")
obj_work_car = WorkCar(44, "черная", "Dodge RAM")
obj_police_car = PoliceCar(110, "спец цвет", "Chevrolet Caprice Classic")

# вывод перечня объектов и их атрибутов
obj_list = [obj_town_car, obj_sport_car, obj_work_car, obj_police_car]
print("Список машин и их атрибутов: \n")
for el in obj_list:
    print(el.__dict__)  # вывод информации в "служебном" формате с использованием словаря параметров и значений
    print(f"Название машины: {el.name}")
    print(f"Цвет машины: {el.color}")
    el.show_speed()
    if el.is_police:
        print("Это полицейская машина \n")
    else:
        print("Это не полицейская машина \n")

# имитация движения каждого автомобиля со случайным количеством и направлением поворотов
for el in obj_list:
    el.go()
    for iterator in range(randint(1, 3)):
        if randint(0, 1) == 0:
            el.turn("направо")
        else:
            el.turn("налево")
    el.stop()
    print("\n")
