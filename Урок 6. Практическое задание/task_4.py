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
        return print(f"{self.color} машина {self.name} поехала!")

    def stop(self):
        return print(f"Машина {self.name} остановилась!")

    def turn(self):
        turn = input("Куда вы хотите повернуть? ('left' или 'right'):")
        if turn == "left":
            print(f"Машина {self.name} поворачивает на лево")
        elif turn == "right":
            print(f"Машина {self.name} поворачивает на право")
        else:
            print(f"Машина {self.name} вылетела в кювет!")

    def police(self):
        if self.is_police == True:
            print("Это полицейская машина!")

    def show_speed(self):
        return print(f"Вы едите со скоростью {self.speed} км/ч.")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return print(f"Вы едите слишком быстро {self.speed} км/ч. , притормозите. Ограничение 60 км/ч!")
        else:
            print("Вы едите с допустимой скоростью.")


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return print(f"Вы едите слишком быстро {self.speed} км/ч. , притормозите. Ограничение 40 км/ч!")
        else:
            print("Вы едите с допустимой скоростью.")


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


tc = TownCar(70, "Синяя", "BMW", False)
tc.go(), tc.police(), tc.show_speed(), tc.turn(), tc.stop()

wk = WorkCar(50, "Зеленая", "Lada", False)
wk.go(), wk.police(), wk.show_speed(), wk.turn(), wk.stop()

sc = SportCar(200, "Красная", "Ferrari", False)
sc.go(), sc.police(), sc.show_speed(), sc.turn(), sc.stop()

pc = PoliceCar(120, "Белая с синим", "Skoda", True)
pc.go(), pc.police(), pc.show_speed(), pc.turn(), pc.stop()