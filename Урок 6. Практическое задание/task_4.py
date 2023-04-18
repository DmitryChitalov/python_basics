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

class Car:# Создаем класс

    def __init__(self, speed, color, name, is_police=False):
        # атрибуты объекта
        self.speed = speed #публичный атрибут
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self): # публичный метод поехала
        print(f"{self.name} поехала")
    def stop(self): # публичный метод остановилась
        print(f"{self.name} остановилась")
    def turn(self, direction): # публичный метод повернула
        print(f"{self.name} повернула {direction}")
    def show_speed(self): # публичный метод показа скорости
        print(f"Скорость {self.name} равна {self.speed}")

class TownCar(Car): # дочерний класс
    def show_speed(self): #
        if self.speed > 60:
            print(f"У {self.name} превышение скорости")
        else: print("Скорость не превышена")

class SportCar(Car): # дочерний класс
    pass

class WorkCar(Car): # дочерний класс
    def show_speed(self):
        if self.speed > 40:
            print(f"У {self.name} превышение скорости")
        else: print("Скорость не превышена")



class PoliceCar(Car): # дочерний класс
    pass
# объект класса и вызов метода
town_car = TownCar(70, "черный", "Рено", False)
town_car.go()
town_car.show_speed()
town_car.turn("налево")
town_car.stop()
# объект класса и вызов метода
sport_car = SportCar(120, "красный", "Жигуль", False)
sport_car.show_speed()
# объект класса и вызов метода
work_car = WorkCar(50, "белый", "Рено", False)
work_car.show_speed()
work_car.turn("налево")
# объект класса и вызов метода
police_car = PoliceCar(90, "синий", "Лада", True)
print(f"Полиция {police_car.is_police}")
