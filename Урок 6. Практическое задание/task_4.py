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
        self.is_police = is_police
    def go(self):
        print(f"Машина {self.name} поехала")
    def stop(self):
        print(f"Машина {self.name} остановилась")
    def turn(self, direction):
        self.direction = direction
        if self.direction == "right":
            print(f"Машина {self.name} повернула направо")
        elif self.direction == "left":
            print(f"Машина {self.name} повернула налево")
        else:
            print(f"Машина {self.name} совершила неизвестный вираж")
    def show_speed(self):
        print(f"Скорость машины {self.name} {self.speed} км/час")

class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > 60:
            print(f"Скорость машины {self.name} превышена!")
        else:
            print(f"Скорость машины {self.name} {self.speed} км/час")

class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > 40:
            print(f"Скорость машины {self.name} превышена!")
        else:
            print(f"Скорость машины {self.name} {self.speed} км/час")

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)

town_car = TownCar(70, "синий", "KIA")
town_car.go()
town_car.show_speed()
sport_car = SportCar(100, "красный", "BMW")
sport_car.show_speed()
sport_car.turn("flight")
sport_car.stop()
work_car = WorkCar(50, "черный", "ГАЗ")
work_car.show_speed()
work_car.turn("left")
police_car = PoliceCar(80, "белый", "Ford")
police_car.show_speed()
police_car.turn("right")
