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

    def police(self):
        if self.is_police:
            print(f'{self.name} - полицейский автомобиль')
        else:
            print(f'{self.name} - гражданский автомобиль')

    def go(self):
        print(f'\n{self.name} начал движение')

    def stop(self):
        print(f'{self.name} остановился')

    def turn(self, direction):
        print(f'{self.name} повернул {direction}')

    def show_speed(self):
        print(f'Скорость {self.name} = {self.speed} км/ч')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f'Превышение скорости')

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f'Превышение скорости')    

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


townCar = TownCar(85, "Синий", "Reno", False)
sportCar = SportCar(210, "Красный", "Lotus", False)
workCar = WorkCar(94, "Красный", "Nissan", False)
policeCar = PoliceCar(190, "Чёрный", "Ford", True)

townCar.go()
townCar.turn("налево")
townCar.show_speed()
townCar.stop()
townCar.police()

sportCar.go()
sportCar.turn("направо")
sportCar.show_speed()
sportCar.stop()
sportCar.police()

workCar.go()
workCar.turn("налево")
workCar.show_speed()
workCar.stop()
workCar.police()

policeCar.go()
policeCar.turn("разворот")
policeCar.show_speed()
policeCar.stop()
policeCar.police()