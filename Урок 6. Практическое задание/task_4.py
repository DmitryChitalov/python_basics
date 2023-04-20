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
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Едем")

    def stop(self):
        print("Стоп!")

    def turn(self, direction):
        def __init__(self, direction):
            self.direction = direction

        print(f"Поворот {direction}")

    def show_speed(self):
        print(f"Скорость: {self.speed}")

    def __str__(self):
        if self.is_police:
            return f"Поездка автомобиля: {self.color} {self.name}, Полиция!!"
        else:
            return f"Поездка автомобиля: {self.color} {self.name}, гражданский авто"


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60 and not self.is_police:
            print("Скорость превышена! ", end='')
        print(f"Скорость: {self.speed}")


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40 and not self.is_police:
            print("Скорость превышена! ", end='')
        print(f"Скорость: {self.speed}")


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


car1 = TownCar(40, 'Белый', 'Hyundai Solaris', False)
car2 = WorkCar(60, 'Белый', 'Lada Granta', False)
car3 = SportCar(200, 'Черный', 'BMW M5', False)
car4 = PoliceCar(70, 'Белый', 'Hyundai Solaris', True)

print(car1)
car1.go()
car1.show_speed()
car1.turn("налево")
car1.go()
car1.speed = 120
car1.show_speed()
car1.stop()
input("Для продолжения нажмите Enter")
print(car2)
car2.go()
car2.show_speed()
car2.speed = 120
car2.show_speed()
car2.turn("налево")
car2.go()
car2.speed = 40
car2.show_speed()
car2.stop()
input("Для продолжения нажмите Enter")
print(car3)
car3.go()
car3.show_speed()
car3.speed = 220
car3.show_speed()
car3.speed = 260
car3.show_speed()
car3.speed = 290
car3.show_speed()
car3.speed = 350
car3.show_speed()
car3.stop()
input("Для продолжения нажмите Enter")
print(car4)
car4.go()
car4.show_speed()
car4.speed = 120
car4.show_speed()
car4.turn("налево")
car4.go()
car4.speed = 40
car4.show_speed()
car4.stop()
