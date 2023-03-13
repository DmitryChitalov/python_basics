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
        print(f"{self.color} {self.name} поехала.")

    def stop(self):
        print(f"{self.color} {self.name} остановилась.")

    def turn(self, direction):
        print(f"{self.color} {self.name} повернула {direction}.")

    def show_speed(self):
        print(f"Текущая скорость {self.color} {self.name}: {self.speed} км/ч.")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"{self.color} {self.name} превысила скорость!")
        else:
            print(f"Текущая скорость {self.color} {self.name}: {self.speed} км/ч.")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"{self.color} {self.name} превысила скорость!")
        else:
            print(f"Текущая скорость {self.color} {self.name}: {self.speed} км/ч.")


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=True)


car1 = TownCar(70, "белая", "Городская машина")
car2 = SportCar(120, "красная", "Спортивная машина")
car3 = WorkCar(30, "серая", "Рабочая машина")
car4 = PoliceCar(90, "черно-белая", "Полицейская машина")

print(car1.speed, car1.color, car1.name, car1.is_police)
print(car2.speed, car2.color, car2.name, car2.is_police)
print(car3.speed, car3.color, car3.name, car3.is_police)
print(car4.speed, car4.color, car4.name, car4.is_police)

car1.go()
car1.turn("направо")
car1.show_speed()

car2.go()
car2.stop()
car2.show_speed()

car3.turn("налево")
car3.show_speed()

car4.go()
car4.show_speed()
