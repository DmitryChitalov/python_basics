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
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Транспорт {self.name} движется")

    def stop(self):
        print(f"Транспорт {self.name} стоит")

    def turn(self, direction):
        print(f"Транспорт {self.name} поворачивает {direction}")

    def show_speed(self):
        print(f"Текущая {self.name} скорость = {self.speed}")


class TownCar(Car):
    def show_speed(self):
        print(f"Превышение скорости 60 км/ч")


class SportCar(Car):
    def type_car(self):
        print(f"{self.name} {self.color} спортивный автомобиль черепахи")


class WorkCar(Car):
    def show_speed(self):
        print(f"Превышение скорости 40 км/ч")


class PoliceCar(Car):
    def type_car(self):
        if self.is_police is True:
            print(f"{self.name} Полицейский автомобиль")
        else:
            print(f"{self.name} Не идентифицированный автомобиль")


result_1 = Car(100, "red", "Toyota")
print(result_1.name)
print(result_1.speed)
print(result_1.color)

result_1.go()
result_1.stop()
result_1.turn("налево")
result_1.turn("направо")

result_1.show_speed()

speed = int(input("Введите скорость: "))

if 40 < speed <= 60:
    result_2 = WorkCar(speed, "green", "Mazda")
    result_2.show_speed()
elif speed > 60:
    result_2 = TownCar(speed, "green", "Mazda")
    result_2.show_speed()
else:
    result_2 = SportCar(speed, "green", "Mazda")
    result_2.type_car()

result_3 = PoliceCar(speed, "white", "Lada", True)
result_3.type_car()
