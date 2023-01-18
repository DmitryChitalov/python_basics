# Реализуйте базовый класс Car.
#у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
#для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("ехать")
    def stop(self):
        print("стоп")

    def turn(self, direction):
        print(f'направление {direction}')

    def show_speed(self):
        print(f'{self.name}  {self.speed}')

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f'{self.name} скорость превышена')
        else:
            print((f'{self.name}  {self.speed}'))


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
           print(f'{self.name} скорость превышена')
        else:
            print((f'{self.name}  {self.speed}'))


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police == True:
            print(f'{self.name} полицейская машина')
        else:
            print("провто машинка")

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


sportcar = SportCar(100, 'Red', 'sportcar', False)
towncar = TownCar(100, 'White', 'towncar', False)
workcar = WorkCar(70, 'Green', 'workcar', True)
policecar = PoliceCar(110, 'Blue',  'policecar', True)

policecar.show_speed()
towncar.show_speed()
workcar.turn('derevnya')
policecar.police()


