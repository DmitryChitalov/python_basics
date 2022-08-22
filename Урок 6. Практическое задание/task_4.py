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


# предопределенные значения направлений поворота
STRAIGHT = 0
LEFT = 1
RIGHT = 2


class Car:
    speed = 0
    max_speed = 90  # максимальная скорость автомобиля
    color = 'nocolor'
    name = 'Car'
    is_police = False
    turn_direction = STRAIGHT  # straight, left, right

    def go(self):
        if self.speed > 0:
            print("Машина поехала!")
        return

    def stop(self):
        if self.speed == 0:
            print("Машина остановилась!")
        return

    def turn(self):
        if self.turn_direction == LEFT:
            print("Автомобиль поворачивает налево")
        elif self.turn_direction == RIGHT:
            print("Автомобиль поворачивает направо")
        else:
            print("Автомобиль едет прямо")
        return

    def show_speed(self):
        print(f"Скорость: {self.speed} км/ч")
        return

    def turn_to(self, direction):
        if direction == LEFT or direction == RIGHT or direction == STRAIGHT:
            self.turn_direction = direction
        else:
            print("Неверный код направления поворота.")
        return


class TownCar(Car):
    name = "Городская машина"
    color = 'silver'
    max_speed = 80

    def show_speed(self):
        if self.speed > 60:
            print(f"Превышение скорости на {self.speed - 60} км/ч")
        return


class SportCar(Car):
    name = "Спорт-кар"
    color = 'red'
    max_speed = 200


class WorkCar(Car):
    name = "Рабочая машина"
    color = 'black'
    max_speed = 60

    def show_speed(self):
        if self.speed > 40:
            print(f"Превышение скорости на {self.speed - 40} км/ч")
        return


class PoliceCar(Car):
    name = "Полицейская машина"
    is_police = True
    color = 'black-white'
    max_speed = 180


car_1 = Car()
car_2 = PoliceCar()
car_3 = TownCar()
car_4 = WorkCar()
car_5 = SportCar()
cars = [car_1, car_2, car_3, car_4, car_5]

for c in cars:
    print(f"Название машины: {c.name}")
    c.speed = 120
    c.show_speed()
    print("Полицейская машина? - ", c.is_police)
    print(f"Цвет автомобиля: {c.color}")
    print(f"Максимальная скорость автомобиля: {c.max_speed} км/ч")
    c.speed = 0
    c.show_speed()
    c.stop()
    c.speed = 100
    c.show_speed()
    c.go()
    c.turn_to(LEFT)
    c.turn()
    c.turn_to(RIGHT)
    c.turn()
    c.turn_to(STRAIGHT)
    c.turn()
    print("")

