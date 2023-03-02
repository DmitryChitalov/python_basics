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
    
    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        
    def go(self):
        print('Машина поехала.')
    
    def stop(self):
        print('Машина остановилась.')
    
    def turn(self, turn):
        if turn == 'left':
            print('Машина повернула на лево.')
        elif turn == 'right':
            print('Машина повернула на право.')
        else:
            print('Машина едет прямо.')
    
    def show_speed(self):
        print(f'Скорость: {self.speed}')


class TownCar(Car):
    
    def show_speed(self):
        print(f'Скорость: {self.speed}')
        if self.speed > 60:
            print('Вы превысили скорость.')

class SportCar(Car):
    
    def __init__(self, speed: int, color: str, name: str, is_police: bool, number_of_wheels: int):
        super().__init__(speed, color, name, is_police)
        self.number_of_wheels = number_of_wheels
    
class WorkCar(Car):
    
    def show_speed(self):
        print(f'Скорость: {self.speed}')
        if self.speed > 40:
            print('Вы превысили скорость.')
    
    def __str__(self):
        show = self.show_speed()
        return f'Скорость:{show}'
        
        

class PoliceCar(Car):
    
    def __init__(self, speed: int, color: str, name: str, is_police: bool, siren: bool):
        super().__init__(speed, color, name, is_police)
        self.siren = siren
    
        
town_car = TownCar(50, "black", 'man', False)
town_car.go()

sport_car = SportCar(100, 'red', 'porsche', False, 4)
print(sport_car.name, sport_car.number_of_wheels)
sport_car.stop()

work_car = WorkCar(50, 'green', 'opel', False)
work_car.__str__()

police_car = PoliceCar(90, 'white', 'bnw', True, True)
print(police_car.is_police, police_car.siren)
police_car.turn('left')