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


haval_jolion = TownCar(60, 'Сапфир', 'Haval Jolion', False)
haval_jolion.go()
haval_jolion.show_speed(50)
haval_jolion.turn('налево')
haval_jolion.go()
haval_jolion.show_speed(70)
haval_jolion.stop()
print()

toyota_camry = WorkCar(80, 'Черный', 'Toyota Camry 70', False)
toyota_camry.go()
toyota_camry.show_speed(60)
toyota_camry.turn('направо')
toyota_camry.go()
toyota_camry.turn('направо')
toyota_camry.show_speed(90)
toyota_camry.stop()
toyota_camry.go()
toyota_camry.show_speed(50)
toyota_camry.turn('налево')
print()

subaru = SportCar(90, 'Хаки', 'Subaru Impreza WRT-X', False)
subaru.go()
# subaru.show_speed(110)
subaru.turn('направо')
subaru.turn('направо')
subaru.go()
subaru.show_speed(180)
subaru.show_speed(210)
subaru.show_speed(230)
print()

lada_prio = PoliceCar(110, 'Белый', 'Lada Priora', True)
lada_prio.go()
lada_prio.show_speed(110)
lada_prio.show_speed(150)
lada_prio.stop()
print()