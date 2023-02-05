'''
4. Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
'''
class Cars:
    def __init__(self, color, name, is_police=False, speed=0):
        self._speed = speed
        self._color = color
        self._name = name
        self._is_police = is_police
        print('*'*50)
        print(f' Автомобиль {self._name} цвет {self._color} !')
        print('*' * 50)

    def go(self):
        print('Старт!')

    def stop(self):
        self._speed = 0
        print('Стоп!')
        self.show_speed()

    def turn(self, direction):
        print(('Не возможно повернуть с нулевой скоростью', f'Поворот {direction}')[self._speed > 0])

    def accelerate(self, acceleration):
        self._speed += acceleration
        self.show_speed()

    def slow_down(self, deceleration):
        self._speed = (0, self._speed - deceleration)[self._speed - deceleration > 0]
        self.show_speed()

    def show_speed(self):
        print(f'Скорость автомобиля {self._speed} км/ч')


class TownCar(Cars):
    def show_speed(self):
        super().show_speed()
        if self._speed > 60:
            print(f'Снизьте скорость!')


class SportCar(Cars):
    pass


class WorkCar(Cars):
    def show_speed(self):
        super().show_speed()
        if self._speed > 40:
            print(f'Снизьте скорость!')


class PoliceCar(Cars):
    pass


tc = TownCar('белый', 'KIA Optima', True)
tc.go()
tc.accelerate(70)
tc.turn('налево')
tc.slow_down(150)
tc.turn('направо')


wc = WorkCar('желтый', 'КАМАЗ')
wc.go()
wc.accelerate(30)
wc.stop()


####
ws = SportCar('красный', 'Ferrari')
wc.go()
wc.accelerate(170)
wc.stop()

pc = PoliceCar('синий', 'Skoda Octavia')
pc.go()
pc.accelerate(60)
pc.stop()
