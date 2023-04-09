class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.name} движется")

    def stop(self):
        print(f"{self.name} остановился")

    def turn(self, direction):
        print(f"{self.name} повернул {direction}")

    def show_speed(self):
        print(f"Текущая скорость {self.name} ровна {self.speed}")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"{self.name} разгоняется! Текущая скорость ровна {self.speed}")
        else:
            print(f"Текущая скорость {self.name} ровна {self.speed}")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"{self.name} разгоняется! Текущая скорость ровна {self.speed}")
        else:
            print(f"Текущая скорость {self.name} ровна {self.speed}")


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


car1 = TownCar(70, 'red', 'Toyota')
car2 = SportCar(120, 'blue', 'Porsche')
car3 = WorkCar(50, 'white', 'Ford')
car4 = PoliceCar(90, 'black', 'Chevrolet')

car1.go()
car2.turn('на право')
car3.show_speed()
print(car4.is_police)

car1.show_speed()
car3.show_speed()

