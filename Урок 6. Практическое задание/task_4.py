"""
Задание 4.

Реализуйте базовый класс Car. У данного класса должны быть следующие публичные атрибуты:
speed, color, name, is_police (булево).

А также публичные методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).

Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.

Добавьте в базовый класс публичный метод show_speed,
который должен показывать текущую скорость автомобиля.

Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    name = 'car'
    is_police = False
    speed = 5.0
    color = 'red'

    def __str__(self):
        return f'Это гражданский автомобиль.' if self.is_police == False else f'Это полицейский автомобиль!'

    def go(self):
        print('Автомобиль начал движение!')

    def stop(self):
        print('Автомобиль остановился!')
   
    def turn(self, direction):
        if direction != 'право' and direction != 'лево':
            print('Неизвестное направление поворота. Используйте "право" или "лево"')
        else:
            print(f'Автомобиль {self.name} повернул на{direction}')

    def show_speed(self):
        print(
            f'Автомобиль {self.name} двигается со скоростью {self.speed} км/ч.')

class TownCar(Car):
    
    def show_speed(self):
        print('Вы превысили скорость! Лимит 60 км/ч') if self.speed > 60 else print(
            f'Автомобиль {self.name} двигается со скоростью {self.speed} км/ч.')

class WorkCar(Car):

    def show_speed(self):
        print('Вы превысили скорость! Лимит 40 км/ч') if self.speed > 40 else print(
            f'Автомобиль {self.name} двигается со скоростью {self.speed} км/ч.')

class PoliceCar(Car):
    is_police = True
    
class SportCar(Car):
    pass

robo_car = PoliceCar()
print(robo_car)
car_n = TownCar()
car_n.name = 'Skoda'
print(car_n)
car_n.go()
car_n.turn('лево')
car_n.turn('право')
car_n.turn('кастрома')
car_n.speed = 60
car_n.show_speed()
car_n.stop()
fast_car = SportCar()
fast_car.speed = 250
fast_car.name = 'Ferrari'
fast_car.color = 'green'
fast_car.show_speed()
print(fast_car.color)
