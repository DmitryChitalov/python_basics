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
        self.is_police = bool(is_police)

    def show_speed(self):
        return f"Текущая скорость автомобиля: {self.speed}"

    def go(self):
        return "Машина поехала"

    def stop(self):
        return "Машина остановилась"

    def turn(self, direction):
        return f"Машина повернула {direction}"


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f"Скорость {self.speed} - это превышение скорости"
        else:
            return f"Текущая скорость автомобиля: {self.speed}"

    def police(self):
        if self.is_police:
            return "Машина полицейская"
        else:
            return "Машина городская"


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return "Машина полицейская"
        else:
            return "Машина спортивная"


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f"Скорость {self.speed} - это превышение скорости"
        else:
            return f"Текущая скорость автомобиля: {self.speed}"

    def police(self):
        if self.is_police:
            return "Машина полицейская"
        else:
            return "Машина рабочая"


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return "Машина полицейская"
        else:
            return "Машина не полицеская"


a = TownCar(80, "Серый", "KIA", False)
b = SportCar(160, "Красный", "Ламборгини", False)
c = WorkCar(20, "Черный", "ВАЗ", False)
d = PoliceCar(150, "Черный", "Lada", True)

print(f'Скорость автомобиля {a.name}: {a.show_speed()}')
print(f'Скорость автомобиля {b.name}: {b.show_speed()}')
print(f'Скорость автомобиля {c.name}: {c.show_speed()}')
print(f'Скорость автомобиля {d.name}: {d.show_speed()}')
print(f'Наименование: {a.name}' '\n'
      f'Цвет: {a.color}' '\n'
      f'Тип машины: {a.police()}')
print(f'Наименование: {b.name}' '\n'
      f'Цвет: {b.color}' '\n'
      f'Тип машины: {b.police()}')
print(f'Наименование: {c.name}' '\n'
      f'Цвет: {c.color}' '\n'
      f'Тип машины: {c.police()}')
print(f'Наименование: {d.name}' '\n'
      f'Цвет: {d.color}' '\n'
      f'Тип машины: {d.police()}')
print(f'{a.name} {a.go()}' '\n'
      f'{a.turn("Направо")}' '\n'
      f'{a.stop()}')
