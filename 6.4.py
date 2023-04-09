class Car:
    speed: int
    color: str
    name: str
    is_police: bool = False

    def __init__(self, speed: int, color: str, name: str) -> None:
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print(f"{self.name}: старт")

    def stop(self):
        print(f"{self.name}: стоп")

    def turn(self, direction: str):
        print(f"{self.name}: поворот - {direction}")

    def show_speed(self):
        print(f"{self.name}: скорость = {self.speed} км/ч")


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f"{self.name}: превышение скорости")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f"{self.name}: превышение скорости")


class PoliceCar(Car):
    is_police: bool = True


cars = [
    SportCar(240, 'red', 'BMW'),
    TownCar(180, 'silver', 'GAZ3102'),
    WorkCar(80, 'white', 'Oka'),
    PoliceCar(170, 'black', 'Mazda'),
]

cars[0].go()
cars[0].turn("направо")
cars[0].stop()

for car in cars:
    car.show_speed()