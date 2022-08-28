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
from random import randint


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала\n')

    def stop(self):
        print('\nМашина остановилась\n')

    def turn(self, direction):
        if direction == 'Право':
            print('Машина выполнила поворот направо')
        elif direction == 'Лево':
            print('Машина выполнила поворот налево')
        elif direction == 'Разворот':
            print('Машина выполнила разворот')
        else:
            print(f'Машина не может выполнить данный({direction}) маневр')

    def show_speed(self):
        print(f'Скорость автомобиля составляет {self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 61:
            print(f'Превышена скорость автомобиля. Ваша скорость {self.speed} '
                  f'км/ч, а должна быть не более 60 км/ч')
        elif self.speed > 0 and self.speed <= 60:
            print(f'У вас допустимая скорость которая равна {self.speed} км/ч')
        else:
            print('Вы еще не начали движение')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 41:
            print(f'Превышена скорость автомобиля. Ваша скорость {self.speed} '
                  f'км/ч, а должна быть не более 40 км/ч')
        elif self.speed > 0 and self.speed <= 40:
            print(f'У вас допустимая скорость которая равна {self.speed} км/ч')
        else:
            print('Вы еще не начали движение')


class PoliceCar(Car):
    pass


tc = TownCar(55, 'Красный', 'Жигули', False)
sc = SportCar(120, 'Черный', 'БМВ', False)
wc = WorkCar(60, 'Желтый', 'Газель', False)
pc = PoliceCar(40, 'Белый', 'Приус', True)
my_dict = {'TownCar': tc, 'SportCar': sc, 'WorkCar':wc, 'PoliceCar': pc}
turn_list = ['Право', 'Лево', 'Разворот']
for i in my_dict:
    print(f'Вы едете на {i} машине. Модель вашей машини {my_dict[i].name},'
          f'цвет вашей машины {my_dict[i].color}')
    my_dict[i].go()
    for j in turn_list:
        a = randint(0, 2)
        my_dict[i].turn(turn_list[a])
    my_dict[i].stop()

tc.show_speed()
wc.show_speed()


