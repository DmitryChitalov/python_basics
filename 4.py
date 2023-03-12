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
    def __init__(
            self,
            speed: [int, float],
            name: str,
            color: str,
            is_police: bool
    ):
        self.speed = speed
        self.name = name
        self.color = color
        self.is_police = is_police

    def go(self) -> str:
        return f'{self.name} движется вперед!'

    def stop(self) -> str:
        return f'{self.name} остановилась!'

    def turn(self, direction: str) -> str:
        return f'{self.name} поворачивает на{direction}'

    def show_speed(self) -> str:
        return f'Скорость движения {self.name} составляет {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(super().show_speed())

        if self.speed > 60:
            return f'Скорость {self.name} превышает допустимую!'
        else:
            return f'Скорость {self.name} в пределах допустимой'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(super().show_speed())

        if self.speed > 40:
            return f'Скорость {self.name} выше допустимой для рабочей машины!'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


if __name__ == '__main__':
    audi = SportCar(100, 'Audi', 'Red', False)
    oka = TownCar(30, 'Oka', 'White', False)
    lada = WorkCar(70, 'Lada', 'Rose', True)
    ford = PoliceCar(110, 'Ford', 'Blue', True)

    print(audi.show_speed())
    print()
    print(oka.show_speed())
    print()
    oka.speed = 90
    print(oka.show_speed())
    print()
    print(oka.turn('лево'))
