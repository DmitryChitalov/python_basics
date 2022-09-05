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
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        print(f'Машина повернула - {direction}')

    def show_speed(self):
        print(f"Скорость {self.name} сейчас: {self.speed}")


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Текущая скорость {self.name} составляет {self.speed}")
        if self.speed > 60:
            print(f"Скорость авто {self.name}  выше, чем позволяют ПДД")
        else:
            print(f"Скорость авто {self.name}  в рамках ПДД")


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Текущая скорость {self.name} составляет {self.speed}")
        if self.speed > 40:
            print(f"Скорость авто {self.name}  выше, чем позволяют ПДД")
        else:
            print(f"Скорость авто {self.name}  в рамках ПДД")


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police == 'True':
            print(f'Автомобиль {PoliceCar.name} является полицейским')


obj2 = Car(200, "yellow", "Mustang", "False")
print(obj2.go())
print(f"Машина {obj2.name} ее скорость -  {obj2.speed} {obj2.turn('на эстакаду')}")

obj3 = WorkCar(50, 'Синий', 'Газель', False)
print(f'Авто {obj3.name} текущая скорость {obj3.show_speed()}')

obj7 = PoliceCar(150, 'Белый', "Форд", 'True')
print(f'Автомобиль - {obj7.name}, полицейский {obj7.is_police}')
