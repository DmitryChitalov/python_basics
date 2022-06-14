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
    def __init__(self, speed, color, name, is_police ):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return (f'{self.name} is started')
    def stop(self):
        return (f'{self.name} is stoped')
    def turn_right(self):
        return (f'{self.name} is turned right')
    def turn_left(self):
        return (f'{self.name} is turned left')
    def show_speed(self):
        return (f'{self.name} speed is {self.speed}')

class TownCar(Car):
    def show_speed(self):
        if self.speed >= 40:
            return (f'speed of town car {self.name} is higher than allow for town car')
        else:
            return (f'Speed of {self.name} is normal for town car')

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)



class WorkCar(Car):
    def show_speed(self):
        print(f'Current speed of work car {self.name} is {self.speed}')

        if self.speed > 60:
            return f'Speed of {self.name} is higher than allow for work car'




class PoliceCar(Car):
    def police(self):
        if self.is_police:
            return f'{self.name} is from police department'
        else:
            return f'{self.name} is not from police department'






BMW = WorkCar(120, 'black', 'BMW', True)
Mers = SportCar(200, 'green', 'Mercedes', False)
Volga = PoliceCar(200, 'white', 'Volga', True)
ford = TownCar(50, 'red', 'Ford', False)
print(BMW.is_police)
print(BMW.show_speed())
print(ford.stop())
print(Volga.police())
print(Mers.turn_left())
