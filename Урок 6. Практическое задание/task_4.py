"""
Задание 4.

Реализуйте базовый класс Car. У данного класса должны быть следующие публичные
атрибуты: speed, color, name, is_police (булево).

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

    @staticmethod
    def go():
        return "Машина поехала"

    @staticmethod
    def stop():
        return "Машина остановилась"

    @staticmethod
    def turn(direction):
        return f"Машина повернула - {direction}"

    def show_speed(self):
        return f"Скорость {self.name} сейчас: {self.speed}"


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
            return f"Скорость авто {self.name}  выше, чем позволяют ПДД"
        else:
            return f"Скорость авто {self.name}  в рамках ПДД"


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police == 'True':
            return f"Автомобиль {self.name} является полицейским"


obj1 = Car(200, 'жёлтый', 'Mustang', 'False')
print(obj1.go())
print(obj1.show_speed())
print(f"Машина {obj1.name} двигалась со скоростью -  "
      f"{obj1.speed} км/ч, на повороте сбросила скорость и"
      f" {obj1.turn('налево')} после чего {obj1.stop()}")

obj2 = WorkCar(50, 'Синий', 'Газель', 'False')
print(f"{obj2.color} авто {obj2.name} движется со скоростью {obj2.speed} км/ч"
      f"\n {obj2.show_speed()}")

obj3 = PoliceCar(150, 'Белый', 'Ford', 'True')
print(f"Автомобиль - {obj3.name}, полицейский {obj3.is_police}")
print(f"{obj3.police()}")
