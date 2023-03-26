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
    # атрибуты
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # методы
    def go(self):
        return f'{self.name} - старт, в движении'

    def stop(self):
        return f'{self.name} - остановка'

    def turn_right(self):
        return f'{self.name} - правый поворот'

    def turn_left(self):
        return f'{self.name} - левый поворот'

    def show_speed(self):
        return f'Скорость {self.name} - {self.speed} км/ч'


# дочерние классы
class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        # print(f'Скорость {self.name} - {self.speed} км/ч')

        if self.speed > 60:
            return f'Скорость {self.name} больше допустимой'
        else:
            return f'Скорость {self.name} допустима для данного типа авто'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        # print(f'Скорость {self.name} - {self.speed} км/ч')

        if self.speed > 40:
            return f'Скорость {self.name} больше допустимой'
        else:
            return f'Скорость {self.name} допустима для данного типа авто'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} - полицицейский атомобиль'
        else:
            return f'{self.name} - гражданский атомобиль'

# клиентский код
toyota = TownCar(50, 'Серый', 'Toyota', False)
bmw = SportCar(300, 'Красный', 'BMW', False)
uaz = WorkCar(50, 'Зеленый', 'УАЗ', True)
skoda = PoliceCar(90, 'Белый', 'Skoda', True)
# вывод на печать
print(f'Авто {toyota.name}, скорость  {toyota.speed}')
print(f'{toyota.go()}. {toyota.show_speed()}')
print(f'Авто {toyota.turn_right()}, авто {bmw.stop()}')
print(bmw.turn_left())
print(f'Авто {bmw.name} скорость {bmw.speed}')
print(f'{uaz.go()}  {uaz.show_speed()}')
print(f'{uaz.name} полициейский авто? {uaz.is_police}')
print(f'{bmw.name} полициейский авто? {bmw.is_police}')
print(uaz.stop())
print(f'Авто {bmw.turn_left()}')
print(skoda.police())
