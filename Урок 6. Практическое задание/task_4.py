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
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')
        self.speed = 0  # 0 скорость при остановке

    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(f'Текущая скорость {self.speed} км/ч')


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=False)

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print("Превышение скорости в 60 км/ч")


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=False)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=False)

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print("Превышение скорости в 40 км/ч")


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=True)


car1 = TownCar(95, 'серый', 'Mazda')
car2 = TownCar(58, 'синий', 'BMW')
car3 = WorkCar(58, 'белый', 'Niva')
car4 = PoliceCar(88, 'белый', 'Toyota')

# доступ к атрибутам
print(car1.speed, car2.color, car3.name, car4.is_police, car3.is_police)

# проверка методов
car1.go()
car2.stop()
car3.turn('Направо')
print()  # пустая строка, для отделния

car1.show_speed()
print()  # пустая строка, для отделения
car2.show_speed()
print()  # пустая строка, для отделения
car3.show_speed()
print()  # пустая строка, для отделения
car4.show_speed()
