class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.color} {self.name} едет со скоростью {self.speed} км")

    def stop(self):
        print(f"{self.color} {self.name} становилась")

    def turn(self, direction):
        print(f"{self.color} {self.name} повернула на {direction}")

    def show_speed(self):
        if self.speed < 80:
            pass
        else:
            print(f"{self.color} {self.name} превысила скорость")


class TownCar(Car):
    def show_speed(self):
        if self.speed < 60:
            pass
        else:
            print(f"{self.color} {self.name} превысила скорость")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed < 40:
            pass
        else:
            print(f"{self.color} {self.name} превысила скорость")


class PoliceCar(Car):
    pass


a = TownCar(70, "Зеленая", "Лада", 80)
a.go()
a.show_speed()
a.turn("лево")
a.turn("право")
a.stop()

b = SportCar(75, "Желтый", "Ламборгини", 80)
b.go()
b.show_speed()
b.turn("право")
b.stop()

d = PoliceCar(90, "Белая", "Буханка", 80)
d.go()
d.show_speed()
d.turn("лево")
d.turn("право")
d.stop()

c = WorkCar(45, "Серебрянная", "Тойота", 80)
c.go()
c.show_speed()

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
