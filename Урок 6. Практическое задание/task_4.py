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


class Car:  # родительский класс
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        if self.speed != 0:
            print(f'{self.color} {self.name} движется')

    def stop(self):
        if self.speed == 0:
            print(f'{self.color} {self.name} не движется')

    def turn(self, direction):
        print(f'{self.color} {self.name} поворачивает на{direction}')

    def show_speed(self):
        print(f'{self.color} {self.name} движется со скоростью {self.speed} км/ч')


class TownCar(Car):  # дочерний класс
    def show_speed(self):
        if self.speed > 60:
            print(f'{self.color} {self.name} превысил(а) скорость 60 км/ч.')
        else:
            print(f'{self.color} {self.name} движется со скоростью {self.speed} км/ч')


class WorkCar(Car):  # дочерний класс
    def show_speed(self):
        if self.speed > 40:
            print(f'{self.color} {self.name} превысил(а) скорость 40 км/ч.')
        else:
            print(f'{self.color} {self.name} движется со скоростью {self.speed} км/ч')


class SportCar(Car):  # дочерний класс
    def attract_attention(self):
        print(f'Все оборачиваются на {self.color} {self.name}')


class PoliceCar(Car):  # дочерний класс
    def intruder(self):
        print(f'Полицейский {self.color} {self.name}. Преследую нарушителя')


tc1 = TownCar(50, 'Зелёная', 'Mazda', False)
tc1.go()
tc1.turn('лево')
tc1.show_speed()
pc1 = PoliceCar(50, 'Белый', 'Ford', True)
sc1 = SportCar(80, 'красный', 'Ferrari', False)
sc1.attract_attention()
sc1.show_speed()
if sc1.speed > 60:
    pc1.intruder()
sc1 = SportCar(40, 'красный', 'Ferrari', False)
sc1.show_speed()
sc1 = SportCar(0, 'красный', 'Ferrari', False)
sc1.stop()
