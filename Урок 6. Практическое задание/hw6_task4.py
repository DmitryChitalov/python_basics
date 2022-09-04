class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        info_1 = "Машина поехала\n"
        return info_1

    def stop(self):
        info_2 = "Машина остановилась\n"
        return info_2

    def turn(self, direction):
        info_3 = f"Машина повернула {direction}\n"
        return info_3

    def show_speed(self):
        return self.speed


class TownCar(Car):
    def __init__(self):
        self.speed = 60
        self.color = 'black'
        self.name = 'Lincoln'
        self.is_police = False

    def show_speed(self):
        if self.speed > 60:
            war = "Скорость превышена!\n"
            return war
        else:
            info_4 = "Допустимая скорость\n"
            return info_4


class SportCar(Car):
    def __init__(self):
        self.speed = 200
        self.color = 'red'
        self.name = 'Porsche'
        self.is_police = False


class WorkCar(Car):
    def __init__(self):
        self.speed = 50
        self.color = 'white'
        self.name = 'Mercedes'
        self.is_police = False

    def show_speed(self):
        if self.speed > 40:
            war = "Скорость превышена!\n"
            return war
        else:
            info_5 = "Допустимая скорость\n"
            return info_5


class PoliceCar(Car):
    def __init__(self):
        self.speed = 100
        self.color = 'blue'
        self.name = 'BMW'
        self.is_police = True


t = TownCar()
print(f"Name: {t.name} \nColor: {t.color} \nSpeed: {t.speed} \nPolice: {t.is_police} \n")
print(t.go())
print(t.show_speed())

s = SportCar()
print(f"Name: {s.name} \nColor: {s.color} \nSpeed: {s.speed} \nPolice: {s.is_police} \n")
print(s.show_speed())
print(s.stop())

w = WorkCar()
print(f"Name: {w.name} \nColor: {w.color} \nSpeed: {w.speed} \nPolice: {w.is_police} \n")
print(w.show_speed())
print(w.turn('направо'))

p = PoliceCar()
print(f"Name: {p.name} \nColor: {p.color} \nSpeed: {p.speed} \nPolice: {p.is_police} \n")
print(p.show_speed())
print(p.turn('назад'))
