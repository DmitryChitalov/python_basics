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

    # methods
    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернула на право'

    def turn_left(self):
        return f'{self.name} повернула на лево'

    def show_speed(self):
        return f'Текущая скорость автомобиля {self.name} равна {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость городского автомобиля {self.name} равна {self.speed}')

        if self.speed > 40:
            return f'Скорость автомобиля {self.name} выше нормы для городского автомобиля'
        else:
            return f'Скорость автомобиля {self.name} нормальна для городского автомобиля'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def sport(self):
        if self.is_police:
            return f'Автомобиль {self.name} является спортивным'
        else:
            return f'Автомобиль {self.name} не является спортивным'


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость рабочего автомобиля {self.name} равна {self.speed}')

        if self.speed > 60:
            return f'Скорость автомобиля {self.name} выше нормы для рабочего автомобиля'
        else:
            return f'Скорость автомобиля {self.name} нормальна для рабочего автомобиля'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'Автомобиль {self.name} является полицейским'
        else:
            return f'Автомобиль {self.name} не является полицейским'


audi = SportCar(100, 'Красная', 'Audi', False)
oka = TownCar(30, 'Белая', 'Ока', False)
lada = WorkCar(70, 'Розовая', 'Лада', True)
ford = PoliceCar(110, 'Синяя', 'Ford', True)

print(f'{lada.color} {lada.go()}')
print(f'{lada.turn_right()}')
print(f'{lada.show_speed()}')
print(audi.show_speed())
print(oka.show_speed())
print(oka.turn_left())
print(ford.police())
print(ford.show_speed())