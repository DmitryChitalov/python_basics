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
class Car():
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала дальше'

    def stop(self):
        return f'{self.name} притормозила'

    def turn(self, direction):
        return f'Машина повернула - {direction}'

    def show_speed(self):
        return f'Cкорость {self.name} составляет {self.speed} км/ч'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Cкорость движениния {self.name} составляет {self.speed} км/ч')

        if self.speed > 60:
            print(f'Скорость авто {self.name} выше, чем позволяют ПДД для города')
        else:
            print(f'Скорость авто {self.name} в пределах городского трафика')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def sport(self):
        if self.is_police:
            return f'Автомобиль {self.name} - это спортивный стиль'
        else:
            return f'Автомобиль {self.name} не является спортивной машиной'

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость рабочей машины {self.name} составляет {self.speed} км/ч')

        if self.speed > 40:
            print(f'Скорость авто {self.name} превышает лимит для грузвого тс')
        else:
            print(f'Авто {self.name} не превышает скорость, установленную для грузового тс')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police == 'True':
            print(f'Автомобиль {PoliceCar.name} является полицейским')

VAZ = TownCar(80, 'баклажан', 'Гранта', True)
print(VAZ.go())
print(f'Авто {VAZ.name} разгоняется со скоростью {VAZ.speed} км/ч')

POR = SportCar(250, 'черный', 'Porsche 911', False)
print(f'Если {POR.go()},то {VAZ.turn("налево")}')
print(f'Когда {POR.name} рванул со скоростью {POR.speed} км/ч, то {VAZ.stop()}')

GAZ = WorkCar(50, 'голубой', 'Газель', False)
print(f'У автомобиля {GAZ.name} текущая скорость {GAZ.show_speed()}')
print(f'{GAZ.name} окрашена в {GAZ.color} цвет')

SKO = PoliceCar(150, 'Белый, надпись ДПС', 'Skoda Octavia', True)
print(f'Автомобиль - {SKO.name}, полицейская машинка? {SKO.is_police}')
print(SKO.show_speed())