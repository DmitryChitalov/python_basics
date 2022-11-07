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
    """
    Базовый класс авто
    """
    def __init__(self, name, color, is_police=False):
        self.name = name
        self.color = color
        self.is_police = is_police
        self.speed = 0

    def go(self, speed):
        """
        заставляет машину двигаться
        :param speed: скорость машины
        """
        self.speed = speed
        print(f"машина {self.name} цвета {self.color} поехала")

    def stop(self):
        """
        останавливет машину
        """
        self.speed = 0
        print(f"машина {self.name} цвета {self.color} остановилась")

    def turn(self, direction):
        """
        изменяет направление движения машины
        :param direction: направление движения машины left/right
        """
        print(f"машина {self.name} цвета {self.color} повернула "
              f"{direction}")

    def show_speed(self):
        """
        печатает текущую скорость машины
        """
        print(f"Текущая скорость: {self.speed}")

    def __str__(self):
        return f"name: {self.name}, color: {self.color}, " \
               f"speed: {self.speed}, " \
               f"police: {'yes' if self.is_police else 'no'}"


class TownCar(Car):
    """
    Городское авто
    """
    def __init__(self, name, color):
        super().__init__(name, color, False)

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f"Превышение скорости на {self.speed - 60}")


class SportCar(Car):
    """
    Спортивное авто
    """
    def __init__(self, name, color):
        super().__init__(name, color, False)


class WorkCar(Car):
    """
    Рабочий автомобиль
    """
    def __init__(self, name, color):
        super().__init__(name, color, False)

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f"Превышение скорости на {self.speed - 40}")


class PoliceCar(Car):
    """
    Полицейская машина
    """
    def __init__(self, name, color):
        super().__init__(name, color, True)


town_car = TownCar("VW Polo", "red")
print(town_car)
town_car.show_speed()
town_car.go(20)
town_car.show_speed()
town_car.go(90)
town_car.show_speed()
town_car.turn("left")
town_car.stop()
town_car.show_speed()
print(f"{town_car.name}({town_car.color}) is police: {town_car.is_police}")

print("\n-----------------------------------------\n")

work_car = WorkCar("МАЗ", "blue")
print(work_car)
work_car.show_speed()
work_car.go(80)
work_car.show_speed()
work_car.turn("right")
work_car.go(30)
work_car.show_speed()
work_car.turn("left")
print(f"{work_car.name}({work_car.color}) is police: {work_car.is_police}")
print(f"{work_car.name}({work_car.color}) current speed is {work_car.speed}")

print("\n-----------------------------------------\n")

sport_car = SportCar("Ford Mustang", "white")
print(sport_car)
sport_car.show_speed()
sport_car.go(170)
sport_car.show_speed()
sport_car.stop()
sport_car.show_speed()
sport_car.go(200)
print(f"{sport_car.name}({sport_car.color}) is police: {sport_car.is_police}")
print(f"{sport_car.name}({sport_car.color}) current speed is {sport_car.speed}")

print("\n-----------------------------------------\n")

police_car = PoliceCar("Toyota Tundra", "black/white")
print(police_car)
police_car.go(90)
police_car.show_speed()
police_car.stop()
police_car.show_speed()
police_car.go(130)
print(f"{police_car.name}({police_car.color}) "
      f"is police: {police_car.is_police}")
print(f"{police_car.name}({police_car.color}) "
      f"current speed is {police_car.speed}")
