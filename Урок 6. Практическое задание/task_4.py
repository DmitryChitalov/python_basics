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

    # Делать два метода считаю не логичным, так как авто оновременно не можеи и стоять и двигаться
    def go_stop(self):
        if self.speed > 0:
            return f"Авто {self.name} цвета {self.color},\nдвижется"
        if self.speed < 0:
            return f"Авто {self.name} цвета {self.color},\nдвижется задним ходом"
        else:
            return f"\nАвто {self.name} цвета {self.color},\nстоит"

    def show_speed(self):
        return f"\nскорость {self.speed} км/ч"

    def turn(self, direction):
        return f"\nавто повернуло {direction}"


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60 and self.is_police != 1:
            return f"\nс привышением скорости на {self.speed - 60} км/ч ({self.speed} км/ч)"
        else:
            return f"\nсо скоростью {self.speed} км/ч"


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40 and self.is_police != 1:
            return f"\nс привышением скорости на {self.speed - 40} ({self.speed} км/ч)"
        else:
            return f"\nсо скоростью {self.speed} км/ч"


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


town = TownCar(80, 'blue', 'Audi', 0)
print(f'1:\n{town.go_stop()}, {town.show_speed()}, {town.turn("в право")}')

sport = SportCar(170, 'red', 'Porshe', 0)
print(f'2:\n{sport.go_stop()}, {sport.show_speed()}, {sport.turn("в лево")}')

work = WorkCar(30, 'red', 'WAZ', 0)
print(f'3:\n{work.go_stop()}, {work.show_speed()}, {work.turn("в никуда)")}')

police = PoliceCar(100, 'yellow', 'Kia', 1)
print(f'4:\n{police.go_stop()}, {police.show_speed()}, {police.turn("кругом")}')
