"""
4. Реализуйте базовый класс Car;
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево);
а также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed: при значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.
"""


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} начинает движение'

    def stop(self):
        return f'{self.name} останавливается'

    def turn_right(self):
        return f'{self.name} поворачивает направо'

    def turn_left(self):
        return f'{self.name} поворачивает налево'

    def show_speed(self):
        return f'Текущая скорость автомобиля {self.name} - {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.name} - {self.speed}')

        if self.speed > 60:
            return f'Автомобиль {self.name} превысил скорость'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.name} - {self.speed}')

        if self.speed > 40:
            return f'Автомобиль {self.name} превысил скорость'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


lamborghini = SportCar(200, 'Желтый', 'Lamborghini', 'Не полицейский')
daewoo = TownCar(90, 'Черный', 'Daewoo', 'Не полицейский')
toyota = WorkCar(70, 'Серебристый', 'Toyota', 'Полицейский')
ford = PoliceCar(110, 'Белый',  'Ford', 'Полицейский')
print(lamborghini.turn_left())
print(ford.stop())
print(f'Цвет {daewoo.name} - {daewoo.color}')
print(toyota.show_speed())
print(daewoo.show_speed())
