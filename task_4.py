class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        if self.speed > 0:
            print("Машина в пути")
        else:
            print("Машина остановилась")

    def stop(self):
        if self.speed < 0:
            print("Машина остановилась")
        else:
            print("Машина в пути")

    def turn(self, direction):
        print(f"Машина повернула {direction}")

    def show_speed(self):
        print(self.speed)

class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed < 60:
            print(self.speed)
        else:
            print("Машина превысила скорость")

class SportCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class Workcar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed < 40:
            print(self.speed)
        else:
            print("Машина превысила скорость")

class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

car_1 = TownCar(70, 'красный', 'Toyota Wish', False)
car_1.show_speed()
car_1.turn('направо')
print(car_1.name)
print(car_1.color)

car_2 = Workcar(55, 'белый', 'Titan', False)
car_2.show_speed()
car_2.go()
print(car_2.is_police)