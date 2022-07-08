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

class Car():
    def __init__(self, name, speed, color, direction, is_police = True):
        self.name = name
        self.speed = speed
        self.color = color
        self.direction = direction
        self.is_police = is_police

    def go(self):
        return f"{self.name} поехала"
    def stop(self):
        return f"{self.name} остановился"
    def turn(self):
        if self.direction == "right":
            return "Машина повернула на право"
        else:
            return "Машина повернула на лево"

    def police_car(self):
        if self.is_police == True:
            return "Это полицейский автомобиль"
        else:
            return "Это гражданский автомобиль"
    def get_full_info(self):
        return f"Автомобиль - {self.name}, цвет: {self.color}, движется со скоростью: {self.speed}"

class TownCar(Car):
    def show_speed(self):
        if self.speed >= 60:
            return f"{self.name} движется с превышением скорости для класса TownCar - {self.speed}"
        else:
            return f"{self.name} движется без превышения скорости для класса TownCar - {self.speed}"

class WorkCar(Car):
    def show_speed(self):
        if self.speed >= 40:
            return f"{self.name} движется с превышением скорости для класса WorkCar - {self.speed}"
        else:
            return f"{self.name} движется без превышения скорости для класса TownCar - {self.speed}"




skoda01 = WorkCar("Octavia", 180, "красный", "rigth", False)
print(skoda01.get_full_info())
print(skoda01.police_car())
print(skoda01.go())
print(skoda01.turn())
print(skoda01.show_speed())
print()
ford01 = TownCar("Focus", 90, "белый", "left", True)
print(ford01.get_full_info())
print(ford01.police_car())
print(ford01.turn())
print(ford01.stop())
print(ford01.show_speed())


