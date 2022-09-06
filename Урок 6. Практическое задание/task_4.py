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
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn(self, direction):
        return f'{self.name} повернула в направлении {direction}'

    def show_speed(self):
        return f'Текущая скорость автомобиля {self.name} составляет {self.speed}'


class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость городского автомобиля {self.name} составляет {self.speed}')

        if self.speed > 60:
            return f'Скорость автомобиля {self.name} выше, чем это позволено для городского автомобиля'
        else:
            return f'Скорость автомобиля {self.name} нормальная для городского автомобиля'


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость рабочего автомобиля {self.name} составляет {self.speed}')

        if self.speed > 40:
            return f'Скорость автомобиля {self.name} выше, чем это позволено для рабочего автомобиля'
        else:
            return f'Скорость автомобиля {self.name} нормальная для рабочего автомобиля'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def sport(self):
        if self.is_police:
            return f'Автомобиль {self.name} является спортивным'
        else:
            return f'Автомобиль {self.name} не является спортивным'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'Автомобиль {self.name} является полицейским'
        else:
            return f'Автомобиль {self.name} не является полицейским'


OKA = TownCar(30, 'Белая', 'Ока', False)
VAZ = WorkCar(70, 'Вишневая', 'Лада', True)
AUDI = SportCar(100, 'Красная', 'Ауди', False)
FORD = PoliceCar(110, 'Белый',  'Форд', True)

print(VAZ.turn("Направо"))
print(f'Когда {OKA.turn("Налево")}, то {AUDI.stop()}')
print(f'{VAZ.go()} со скоростью {VAZ.show_speed()}')
print(f'{VAZ.name} цвета {VAZ.color}')

print(f'{AUDI.name} полицейская машина? {AUDI.is_police}')
print(f'{VAZ.name} полицейская машина? {VAZ.is_police}')

print(AUDI.show_speed())
print(OKA.show_speed())
print(FORD.police())
print(FORD.show_speed())
