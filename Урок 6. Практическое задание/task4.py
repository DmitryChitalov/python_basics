class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        return "Машина поехала"
    def stop(self):
        return "Машина остановилась"
    def turn(self, direction):
        return "Машина повернула " + direction
    def show_speed(self):
        return "Машина едет со скоростью " + str(self.speed)

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        if self.speed > 60:
            return "Машина едет со скоростью " + str(self.speed) + " Превышена скорость!"
        else:
            return "Машина едет со скоростью " + str(self.speed)

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        if self.speed > 40:
            return "Машина едет со скоростью " + str(self.speed) + " Превышена скорость!"
        else:
            return "Машина едет со скоростью " + str(self.speed)

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

a = TownCar(100, "Red", "Audi", False)
b = SportCar(200, "Blue", "Lada", False)
c = WorkCar(50, "Grey", "BMW", False)
d = PoliceCar(100, "Pink", "Bugatti", True)
print(f"Параметры городской машины: Cкорость - {a.speed}, Цвет - {a.color}, Название - {a.name}, Полицейская - {a.is_police}".format())
print(f"Параметры спортивной машины: Cкорость - {b.speed}, Цвет - {b.color}, Название - {b.name}, Полицейская - {b.is_police}".format())
print(f"Параметры рабочей машины: Cкорость - {c.speed}, Цвет - {c.color}, Название - {c.name}, Полицейская - {c.is_police}".format())
print(f"Параметры полицейской машины: Cкорость - {d.speed}, Цвет - {d.color}, Название - {d.name}, Полицейская - {d.is_police}".format())
print(a.go())
print(b.turn("на право"))
print(c.stop())
print(f"Скорость полицейской машины: {d.show_speed()}".format())
print(f"Скорость городской машины: {a.show_speed()}".format())
print(f"Скорость рабочей машины: {c.show_speed()}".format())