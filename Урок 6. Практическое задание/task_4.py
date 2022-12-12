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
    """Базовый класс Кар"""
    speed: float
    color: str
    name: str
    is_police: bool

    def go(self):
        """Метод ехать"""
        print(f"Автомобиль {self.name} начал движение")

    def stop(self):
        """Метод остановиться"""
        print(f"Автомобиль {self.name} завершил движение")

    def turn(self, direction):
        """Метод повернуть"""
        print(f"Автомобиль {self.name} в процессе движение сделал поворот {direction}")

    def show_speed(self):
        """Возвращаем скорость"""
        return f"Скорость автомобиля класса '{self.__doc__}' составляет {self.speed} км.ч.\n"
    
    def __str__(self):
        "Возвращаем текст о модели авто"
        if self.is_police:
            police = "Полицейский автомобить"
        else:
            police = "не Полицейский автомобить"
        
        return f"На дороге появился автомобить класса '{self.__doc__}'\n"\
            f"Название авто: {self.name}, Цвет: {self.color}, Тип авто: {police}"


class TownCar(Car):
    """Дочерний класс TownCar"""

    def show_speed(self):
        """Возвращаем скорость TownCar"""
        if self.speed > 60:
            more_speed = self.speed - 60
            return f"Автомобиль класса '{self.__doc__}' превышает скорость\n"\
                f"Он едет со скоростью {self.speed}, что превышает на {more_speed} км.ч.\n"
        else:
            return f"Скорость автомобиля класса '{self.__doc__}' "\
                    f"составляет {self.speed} км.ч.\n"


class SportCar(Car):
    """Дочерний класс SportCar"""
    pass


class WorkCar(Car):
    """Дочерний класс WorkCar"""

    def show_speed(self):
        """Возвращаем скорость WorkCar"""
        if self.speed > 40:
            more_speed = self.speed - 40
            return f"Автомобиль класса '{self.__doc__}' превышает скорость\n"\
                f"Он едет со скоростью {self.speed}, что превышает на {more_speed} км.ч.\n"
        else:
            return f"Скорость автомобиля класса '{self.__doc__}' "\
                    f"составляет {self.speed} км.ч.\n"


class PoliceCar(Car):
    """Дочерний класс PoliceCar"""
    pass


car_1 = WorkCar()
car_1.speed = 47
car_1.color = "Серобуромалиновый"
car_1.name = "Очень универсайльный"
car_1.is_police = False

car_2 = PoliceCar()
car_2.speed = 60.3
car_2.color = "Бело-Синий"
car_2.name = "Страж порядка"
car_2.is_police = True

print(car_1.__str__())
car_1.go()
car_1.turn('направо')
car_1.turn('налево')
car_1.stop()
print(car_1.show_speed())

print(car_2.__str__())
print(car_2.show_speed())
