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
    def __init__ (self, color: str, name: str, is_police: bool = False):
        self.color = color
        self.speed = 0
        self.name = name
        self.is_police = True if is_police else False
        self.direction = ' '

    def go (self, speed: int):
        try:
            self.speed = int(speed)
        except ValueError:
            pass

    def stop (self):
        self.speed = 0

    def turn (self, direction: str):
        if direction not in ('направо', 'налево'):
            print(f"Направление '{direction}' не предусмотрено")
            return
        if not self.speed:
            print(f"Не могу повернуть {direction} на месте")
            return
        self.direction = direction

    def show_speed (self):
        print(f"Моя текущая скорость - {self.speed} км/ч")

    def direction (self):
        return self.direction


class TownCar(Car):
    _max_speed = 60

    def __init__ (self, *args):
        super().__init__(*args)

    def show_speed (self):
        super().show_speed()
        if self.speed > self._max_speed:
            print('Ваша скорость выше допустимой')


class SportCar(Car):
    def __init__ (self, *args):
        super().__init__(*args)


class WorkCar(Car):
    _max_speed = 40

    def __init__(self, *args):
        super().__init__(*args)

    def show_speed (self):
        super().show_speed()
        if self.speed > self._max_speed:
            print('Ваша скорость выше допустимой')
class PoliceCar(Car):
    def __init__(self, *args):
        super().__init__(*args, is_police=True)


if __name__ == '__main__':
    cars_data = {
        ('Yellow', 'Aston Martin Cygnet'): TownCar,
        ('Green', 'BMW M3'): SportCar,
        ('White', 'VAZ 2106'): WorkCar,
        ('Red', 'Ford Crown Victoria'): PoliceCar,
    }

    for car_descr, car_cls in cars_data.items():
        car = car_cls(*car_descr)

        print(f"Марка машины -'{car.name}'")
        print(f"Цвет машины - '{car.color}'")
        print(f"Полицейская ли машина? - '{car.is_police}'")
        print(f"Скорость - '{car.speed}'")
        print(f"Направление - '{car.direction}'")
        print(f"Текущая скорость машины - '{car.show_speed()}'")

        car.turn('asd')
        car.turn('налево')
        car.go('asd')
        print("Скорость автомобиля после недопустимого движения - ", car.speed)
        car.go(30)
        car.show_speed()
        car.go(45)
        car.show_speed()
        car.go(75)
        car.show_speed()
        car.turn('налево')
        print(f"Направление машины - '{car.direction}'")
        car.turn('направо')
        print(f"Направление машины - '{car.direction}'")
        car.stop()
        car.show_speed()
