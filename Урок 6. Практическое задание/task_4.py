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

    def __init__(self, max_speed, color, name, is_police):
        self.max_speed = max_speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Начало движения {self.name}')

    def stop(self):
        print(f'Остановка {self.name} ')

    def turn(self, direction):
        print(f'{self.name} поворачивает {direction}')

    def show_speed(self, speed):
        print(f'Скорость движения автомобиля - {self.speed}')
        if self.speed > self.max_speed and not self.is_police:
            print(f'Автомобиль {self.name} превысил скорость')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self, speed):
        self.speed = speed
        super().show_speed(self.speed)


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self, speed):
        self.speed = speed
        super().show_speed(self.speed)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self, speed):
        self.speed = speed
        super().show_speed(self.speed)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self, speed):
        self.speed = speed
        super().show_speed(self.speed)


emobil = TownCar(60, 'Желтый', 'Ёмобиль', False)
emobil.go()
emobil.show_speed(50)
emobil.turn('налево')
emobil.go()
emobil.show_speed(70)
emobil.stop()
print()

toyota = WorkCar(80, 'Серый', 'Toyota', False)
toyota.go()
toyota.show_speed(60)
toyota.turn('направо')
toyota.go()
toyota.turn('направо')
toyota.show_speed(90)
toyota.stop()
toyota.go()
toyota.show_speed(50)
toyota.turn('налево')
print()

lada_sport = SportCar(90, 'Зелёный', 'Lada Kalina Sport', False)
lada_sport.go()
# subaru.show_speed(110)
lada_sport.turn('направо')
lada_sport.turn('направо')
lada_sport.go()
lada_sport.show_speed(180)
lada_sport.show_speed(210)
lada_sport.show_speed(230)
print()

lada_vesta = PoliceCar(110, 'Белый', 'Lada Vesta', True)
lada_vesta.go()
lada_vesta.show_speed(110)
lada_vesta.show_speed(150)
lada_vesta.stop()
print()
