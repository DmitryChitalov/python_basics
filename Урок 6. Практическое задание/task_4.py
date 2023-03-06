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
        print(f"{self.name} поехала.")
    
    def stop(self):
        print(f"{self.name} остановилась.")
    
    def turn(self, direction):
        print(f"{self.name} повернула {direction}.")
    
    def show_speed(self):
        print(f"Текущая скорость {self.name}: {self.speed} км/ч.")
    

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"{self.name} превысила скорость на {self.speed - 60} км/ч!")
        else:
            super().show_speed()


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"{self.name} превысила скорость на {self.speed - 40} км/ч!")
        else:
            super().show_speed()


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


car1 = TownCar(70, "красный", "Москвич")
car2 = SportCar(120, "черный", "Феррари")
car3 = WorkCar(50, "желтый", "Газель")
car4 = PoliceCar(100, "белый", "Шевроле")

car1.go()
car2.show_speed()
car3.turn("направо")
car4.stop()

