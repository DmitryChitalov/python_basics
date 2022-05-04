class Car:
    def __init__(self, speed, color, name, is_police):
        try:
            self.speed = speed
            self.color = color
            self.name = name
            self.is_police = bool(is_police)
        except BaseException:
            return "Error. Please, enter data."
            exit(-1)
    def go(self):
        return "Go."
    def stop(self):
        return "Stop."
    def turn_left(self):
        return "Turn left."
    def turn_right(self):
        return "Turn right."
    def show_speed(self):
        print("Machine normal speed.")
class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        if self.speed > 40:
            return "Over speed."
        else:
            return "Normal speed"
class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        if self.speed > 60:
            return "Over speed."
        else:
            return "Normal speed"
class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
toyota = SportCar(100, 'Red', 'Toyota', False)
mazda = TownCar(30, 'White', 'Mazda', True)
suzuki = WorkCar(70, 'Rose', 'Suzuki', False)
honda = PoliceCar(110, 'Blue',  'honda', True)
print(toyota.turn_left())
print(mazda.turn_right())
print(suzuki.stop())
print(honda.go())
print(suzuki.is_police)
print(honda.is_police)
print(suzuki.show_speed())
print(honda.show_speed())
