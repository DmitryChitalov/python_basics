class Car:

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'Машина: {self.name} поехала.'

    def stop(self):
        return f'\nМашина {self.name} остановилась.'

    def turn(self, direction):
        return f'\nМашина {self.name} повернула {direction}.'

    def show_speed(self):
        return f'\nСкорость машины равна: {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\nВы превысили скорость. Она равна: {self.speed}.'
        else:
            return f'Скорость машины {self.name} в норме допустимого.'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nВы превысили скорость. Она равна: {self.speed}.'
        else:
            return f'Скорость машины {self.name} в норме допустимого.'


class PoliceCar(Car):
    pass


town = TownCar('Audi', 70, 'blue', False)
print('1:\n' + town.go(), town.show_speed(), town.turn('налево'), town.turn('направо'), town.stop())

sport = SportCar('Formula', 170, 'red', False)
print('2:\n' + sport.go(), sport.show_speed(), sport.turn('налево'), sport.stop())

work = WorkCar('WAZ', 30, 'red', False)
print('3:\n' + work.go(), work.show_speed(), work.turn('направо'), work.stop())

police = PoliceCar('Lada', 100, 'yellow', True)
print('4:\n' + work.go(), work.show_speed(), work.turn('направо'), work.stop())