class Car:
    def __init__(self, speed, color, name, is_police, is_sport=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)
        self.is_sport = bool(is_sport)

    def go(self):
        return "Двигаемся вперед"

    def stop(self):
        return "Остановка"

    def turn(self, direction):
        return f"{self.name} совершает поворот {direction}"

    def show_speed(self):
        return f"Скорость равна {self.speed}"


class TownCar(Car):
    def show_speed(self):
        print(f"Скорость {self.name} равна {self.speed}")
        if self.speed > 60:
            return f"Превышение скорости"


class SportCar(Car):
    def sport(self):
        if self.is_sport == True:
            return f"{self.name} является спортивным автомобилем"
        else:
            return f"{self.name} не является спортивным автомобилем"


class WorkCar(Car):
    def show_speed(self):
        print(f"Скорость {self.name} равна {self.speed}")
        if self.speed > 40:
            return f"Превышение скорости"


class PoliceCar(Car):
    def police(self):
        if self.is_police:
            return f"Автомобиль {self.name} является полицейским"
        else:
            return f"Автомобиль {self.name} не является полицейским"


VAZ = TownCar(100, "Баклажан", "Лада", False)
IV = WorkCar(120, "Белый", "Iveco", False)
DOD = PoliceCar(240, "Чёрный", "Dodge", True)
Lamb = SportCar(300, "Жёлтый", "Lamborghini", False, True)
lamba = SportCar(30, "Жёлтый", "Lamborgoga", False)
print(VAZ.show_speed())
print(IV.show_speed())
print(DOD.turn("налево"))
print(DOD.police())
print(Lamb.sport())
print(lamba.sport())
