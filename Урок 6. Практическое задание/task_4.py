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
        self.is_police = bool(is_police)

    def go(self):
        return f'Автомобиль {self.name} поехал'

    def stop(self):
        return f'Автомобиль {self.name} остановился'

    def turn(self, direction):
        return f'Автомобиль {self.name} повернул {direction}'

    def show_speed(self):
        return f'Скорость автомобиля {self.name}: {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return 'Превышение скорости!'
        else:
            return f'Скорость автомобиля {self.name}: {self.speed}'

    def __str__(self):
        return 'Городской автомобиль'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def __str__(self):
        return 'Спортивный автомобиль'


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return 'Превышение скорости!'
        else:
            return f'Скорость автомобиля {self.name}: {self.speed}'

    def __str__(self):
        return 'Рабочий автомобиль'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police != True:
            return 'НЕ Полицейская машина'
        else:
            return 'Полицейская машина'

    def __str__(self):
        return 'Полицейский автомобиль'


car1 = Car(70, 'Red', 'Nissan', False)
car_pol = PoliceCar(100, 'White', 'Ford', True)
car_town = TownCar(70, 'Grey', 'BMW', False)
car_sport = SportCar(240, 'Blue', 'Ferrari', False)
print(f'Автомобиль: {car1.name} \nЦвет: {car1.color}\n'
      f'Скорость: {car1.speed}км/ч')
print(f'Автомобиль {car_pol.name}, движется со скоростью {car_pol.speed}')
print(car_pol.name, car_pol.police())
print(car_town.name, car_town)
print(car_town.show_speed())
print(car_sport.turn("Налево"))
