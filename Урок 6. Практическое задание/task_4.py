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
    speed: int
    color: str
    name: str
    is_police = False

    def go(self):
        return print(f"Машина поехала")

    def stop(self):
        return print(f"Машина остановилась")

    def turn(self, direction):
        return print(f"Машина повернула {direction}")

    def show_speed(self):
        return print(f"Скорость машины:  {self.speed} км/ч")

    def __init__(self, speed):
        self.speed = speed


class TownCar(Car):
    color = "yellow"
    name = "Volvo"

    def show_speed(self):
        if self.speed > 60:
            return print("Вы превышаете скорость!")
        else:
            return print(f"Скорость машины:  {self.speed} км/ч")


class SportCar(Car):
    color = "red"
    name = "ferrari"


class WorkCar(Car):
    color = "green"
    name = "bmw"

    def show_speed(self):
        if self.speed > 40:
            return print("Вы превышаете скорость!")
        else:
            return print(f"Скорость машины:  {self.speed} км/ч")


class PoliceCar(Car):
    name = "UAZ"
    color = "blue"
    is_police = True


town = TownCar(39)  # Нужно передать значение скорости
print(
    f"Машинка town. Скорость {town.speed}. Цвет {town.color}. Название {town.name}. Является ли полицейской {town.is_police}")
town.show_speed()
town.speed = 90  # Назначаем скорость = 90
town.show_speed()
town.go()
town.stop()
town.turn("Налево")  # Нужно передать строку, обозначающее направление поворота

sport = SportCar(100)
print(
    f"\nМашинка sport. Скорость {sport.speed}. Цвет {sport.color}. Название {sport.name}. Является ли полицейской {sport.is_police}")
sport.show_speed()
sport.go()
sport.stop()
sport.turn("Направо")  # Нужно передать строку, обозначающее направление поворота

work = WorkCar(50)
print(
    f"\nМашинка work. Скорость {work.speed}. Цвет {work.color}. Название {work.name}. Является ли полицейской {work.is_police}")
work.show_speed()

police = PoliceCar(80)
print(
    f"\nМашинка police. Скорость {police.speed}. Цвет {police.color}. Название {police.name}. Является ли полицейской {police.is_police}")
