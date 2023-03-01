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
class Cars:
    def __init__(self, color, name, is_police=False, speed=0):
        self._speed = speed
        self._color = color
        self._name = name
        self._is_police = is_police
        print('*'*50)
        print(f'There is a new {self._color} car {self._name}!')
        print('*' * 50)

    def go(self):
        print('Start driving!')

    def stop(self):
        self._speed = 0
        print('Stop driving!')
        self.show_speed()

    def turn(self, direction):
        print(('Cannot turn with zero speed', f'Turn to {direction}')[self._speed > 0])

    def accelerate(self, acceleration):
        self._speed += acceleration
        self.show_speed()

    def slow_down(self, deceleration):
        self._speed = (0, self._speed - deceleration)[self._speed - deceleration > 0]
        self.show_speed()

    def show_speed(self):
        print(f'The current speed is {self._speed}')


class TownCar(Cars):
    def show_speed(self):
        super().show_speed()
        if self._speed > 60:
            print(f'Please, slow down!')


class SportCar(Cars):
    pass


class WorkCar(Cars):
    def show_speed(self):
        super().show_speed()
        if self._speed > 40:
            print(f'Please, slow down!')


class PoliceCar(Cars):
    pass


pc = PoliceCar('red', 'Robocop', True)
pc.go()
pc.accelerate(20)
pc.turn('left')
pc.slow_down(150)
pc.turn('right')


wc = WorkCar('brown', 'Mat')
wc.go()
wc.accelerate(50)
wc.stop()
