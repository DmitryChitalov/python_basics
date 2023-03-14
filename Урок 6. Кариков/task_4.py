
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed # скорость
        self.color = color # цвет
        self.name = name # название машины
        self.is_police = is_police # является ли машина полицейской

    def go(self):
        print(f"{self.color} {self.name} поехала")

    def stop(self):
        print(f"{self.color} {self.name} остановилась")

    def turn(self, direction):
        print(f"{self.color} {self.name} повернула {direction}")

    def show_speed(self):
        print(f"Текущая скорость {self.color} {self.name}: {self.speed}")

class TownCar(Car):
    def show_speed(self):
        super().show_speed() # вызываем родительский метод
        if self.speed > 60: # проверяем скорость
            print("Внимание! Превышение скорости!")

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        super().show_speed() # вызываем родительский метод
        if self.speed > 40: # проверяем скорость
            print("Внимание! Превышение скорости!")

class PoliceCar(Car):
    pass

# создаем экземпляры классов и передаем значения атрибутов
town_car = TownCar(70, "Красный", "Town Car", False)
sport_car = SportCar(100, "Черный", "Sport Car", False)
work_car = WorkCar(50, "Белый", "Work Car", False)
police_car = PoliceCar(90, "Синий", "Police Car", True)

# выводим значения атрибутов экземпляров
print(f"{town_car.color} {town_car.name}: {town_car.speed}")
print(f"{sport_car.color} {sport_car.name}: {sport_car.is_police}")
print(f"{work_car.color} {work_car.name}: {work_car.is_police}")
print(f"{police_car.color} {police_car.name}: {police_car.speed}")

# вызываем методы экземпляров
town_car.go()
sport_car.turn("направо")
work_car.show_speed()
police_car.stop()