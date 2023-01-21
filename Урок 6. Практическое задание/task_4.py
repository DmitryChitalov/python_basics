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
        return f'{self.name} повернула по напрвелнию {direction}'

    def show_speed(self):
        return f'Скорость машины {self.name} составляет {self.speed}'

class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость TownCar {self.name} составляет {self.speed}')

        if self.speed > 60:
            return f'Автомобиль превысил скорость {self.name}'
        else:
            return f'Автомобиль {self.name} не превысил скорость'


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость WorkCar {self.name} составляет {self.speed}')

        if self.speed > 40:
            return f'Автомобиль превысил скорость {self.name}'
        else:
            return f'Автомобиль {self.name} не превысил скорость'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def sport(self):
        if self.is_police:
            return f'SportCar {self.name}'
        else:
            return f'Автомобиль {self.name} не является SportCar'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'Полицейская машина {self.name}'
        else:
            return f'Автомобиль {self.name} не является PoliceCar'

Hyundai = TownCar(80, 'Grey', 'Hyundai', False)
Chevrolet_Cobalt = WorkCar(70, 'Green', 'Chevrolet_Cobalt', True)
Mercedes = SportCar(120, 'Black', 'Mercedes', False)
Volkswagen = PoliceCar(140, 'White',  'Volkswagen', True)

print(f'{Chevrolet_Cobalt.turn("Налево")}, {Mercedes.stop()}')
print(Hyundai.turn("Направо"))
print(f'{Hyundai.go()} со скоростью {Hyundai.show_speed()}')
print(f'{Hyundai.name} цвета {Hyundai.color}')

print(f'{Mercedes.name} полицейская машина? {Mercedes.is_police}')
print(f'{Volkswagen.name} полицейская машина? {Volkswagen.is_police}')

print(Hyundai.show_speed())
print(Chevrolet_Cobalt.show_speed())
print(Volkswagen.police())
print(Volkswagen.show_speed())