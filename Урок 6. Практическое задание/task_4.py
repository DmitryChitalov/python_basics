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
    """ Базовый класс автомобиля """
    def __init__(
            self,
            color: str,
            name: str,
            is_police: bool = False
    ):
        """
        :param color: Цвет авто
        :param name: Модель (название) авто
        :param is_police: Признак полицейности
        """
        self.color = color
        self.name = name
        self.is_police = True if is_police else False

        self.speed = 0
        self._direction = ''

    def go(self, speed: float):
        """ Начинает движение авто с заданной скоростью
        :param speed: Скорость движения
        """
        try:
            self.speed = float(speed)
        except ValueError:
            pass

    def stop(self):
        """ Останавливает авто """
        self.speed = 0

    def turn(self, direction: str):
        """ Задает поворот авто в движении
        :param direction: направление поворота ('left', 'right')
        """
        if direction not in ('left', 'right'):
            print(f"'{direction}' invalid direction")
            return

        if not self.speed:
            print(f"'Can't turn to {direction}' in place")
            return

        self._direction = direction

    def show_speed(self):
        """ Показать текущуую скорость """
        print(f'My speed is {self.speed} km/h')

        if (hasattr(self, '_max_granted_speed')
                and self._max_granted_speed
                and self.speed > self._max_granted_speed):
            print(f'Over speed on {self.speed - self._max_granted_speed} km/h')

    @property
    def direction(self):
        """ Показать текущее направление """
        return self._direction


class TownCar(Car):
    """ Класс городских автомобилей """
    # максимальная скорость движения
    _max_granted_speed = 60


class SportCar(Car):
    """ Класс спортивный автомобилей """
    pass


class WorkCar(Car):
    """ Класс авто для работы """
    # максимальная скорость движения
    _max_granted_speed = 40


class PoliceCar(Car):
    """ Класс полицейского авто """
    def __init__(self, *args):
        """
        :param args: Параметры авто
        """
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

        print('#######################################')
        print(f"Car name '{car.name}'")
        print(f"Car color '{car.color}'")
        print(f"Car is police '{car.is_police}'")
        print(f"Car speed '{car.speed}'")
        print(f"Car direction '{car.direction}'")
        print(f"Car show speed '{car.show_speed()}'")

        car.turn('asd')
        car.turn('left')
        car.go('asd')
        print("Car speed after invalid go", car.speed)
        car.go(30)
        car.show_speed()
        car.go(45)
        car.show_speed()
        car.go(75)
        car.show_speed()
        car.turn('left')
        print(f"Car direction '{car.direction}'")
        car.turn('right')
        print(f"Car direction '{car.direction}'")
        car.stop()
        car.show_speed()
        print('#######################################\n\n')

