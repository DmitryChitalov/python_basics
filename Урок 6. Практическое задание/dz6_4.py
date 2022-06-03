#  Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

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
        return f'{self.name} повернула направо'

    def turn_left(self):
        return f'{self.name} повернула налево'

    def show_speed(self):
        return f'Скорость {self.name} {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость машины в городе {self.name} {self.speed}')

        if self.speed > 40:
            return f'Скорость {self.name} выше чем допустимая'
        else:
            return f'Скорость {self.name} в пределах нормы'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость рабочей машины {self.name} {self.speed}')

        if self.speed > 60:
            return f'Скорость {self.name} выше допустимой для рабочей машины'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} из полиции'
        else:
            return f'{self.name} обычная машина'


suzuki = SportCar(100, 'белая', 'Сузуки', False)
toyota = TownCar(30, 'серая', 'Тойота', False)
lexus = WorkCar(70, 'белый', 'Лексус', True)
lexus2 = PoliceCar(110, 'черный', 'Лексус', True)
print(lexus.turn_left())
print(f'Когда {toyota.turn_right()}, тогда {suzuki.stop()}')
print(f'{lexus.go()}, {lexus.show_speed()}')
print(f'{lexus.name} {lexus.color}')
print(f'{suzuki.name} полиция? {suzuki.is_police}')
print(f'{lexus.name}  полиция? {lexus.is_police}')
print(suzuki.show_speed())
print(toyota.show_speed())
print(lexus2.police())
print(lexus2.show_speed())
