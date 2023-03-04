class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')
    def turn(self, direction: str):
        print(f'Машина {self.name} повернула {direction}.')

    def show_speed(self):
        print(f'Текущая скорость равна {self.speed} км/ч')

    def police_car(self):
        if self.is_police == True:
            print('Это полицейская машина')
        else:
            print('Это обычная машина')

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        if self.speed > 60:
            print("Скорость превышена")
        else:
            print(self.speed)

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        if self.speed > 40:
            print("Скорость превышена")
        else:
            print(self.speed)

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

car_t = TownCar(60, 'red', 'Автобус', False)
car_s = SportCar(120, 'red', 'Болид', False)
car_w = WorkCar(45, 'red', 'Фургон', False)
car_p = PoliceCar(100, 'red', 'Бобик', True)

car_t.show_speed()
car_s.police_car()
car_w.go()
car_p.turn('Влево')
