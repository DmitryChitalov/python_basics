"""
Заroad_length класс TrafficLight (светофор)
и определить у него один приватный атрибут color (цвет) и публичный метод running (запуск).
В рамках метода running реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.
Для имитации "горения" каждого цвета испольщуйте ф-цию sleep модуля time
Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""
import time


class TrafficLight:
    def running(self):
        __color = "red"
        print(__color)
        time.sleep(7)
        __color = "yellow"
        print(__color)
        time.sleep(2)
        __color = "green"
        print(__color)
        time.sleep(10)


traffic_light = TrafficLight()
traffic_light.running()

"""
Задание 2.
Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
length (длина в метрах), width (ширина в метрах).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
Массу и толщину сделать публичными атрибутами.
Проверить работу метода.
Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т
"""


class Road:

    def __init__(self):
        print("Создаем экземпляр")
        self._road_length = int(input('Введите длину дороги'))
        self._road_width = int(input('Введите ширину дороги'))

    def calculate_weight_of_road(self):
        weight_for_metr = int(input('Введите массу асфальта для покрытия 1 метра дороги'))
        thickness = float(input('Введите толщину дороги'))
        weight = weight_for_metr * thickness * piece_of_road._road_width * piece_of_road._road_length
        print(f'Всего Вам потребуется {weight}кг асфальта')


piece_of_road = Road()
piece_of_road.calculate_weight_of_road()

"""
Задание 3.
Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker. В классе Position реализовать публичные методы
получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку str
__str__(self) - вызывается функциями str, print и format. Возвращает строковое представление объекта.
"""


class Worker:
    def __init__(self):
        self.name = input('Введите имя')
        self.surname = input('Введите фамилию')
        self.position = input('Введите должность')
        wage = int(input('Введите размер ЗП'))
        bonus = int(input('Введите размер премии'))
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(f'Сотрудник: {self.name} {self.surname}')

    def get_total_income(self):
        total_income = self._income['wage'] + self._income['bonus']
        #      print(f'К выплате: {total_income}')
        return f'К выплате: {total_income}'

    def __str__(self):
        return f'Сотрудник: {self.name} {self.surname}, {self.get_total_income()}'


good_worker = Position()
good_worker.get_full_name()
print(good_worker.get_total_income())
print(good_worker)

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
    def __init__(self):
        self.speed = int(input('Укажите скорость'))
        self.color = input('Задайте цвет')
        self.name = input('Как Вашу машинку зовут?')
        self.is_police = bool(input('Это машина спец служб?'))

    def go(self):
        print(f'{self.name}  поехала')

    def stop(self):
        print(f'{self.name}  остановилась')

    def turn_right(self):
        print(f'{self.name}  ----------->')

    def turn_left(self):
        print(f'{self.name}  <-----------')

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.name} составляет {self.speed}')


class TownCar(Car):
    def show_speed(self):
        print(f'Текущая скорость  {self.name} составляет {self.speed}')
        if self.speed > 60:
            print('Вы превышаете!')
        else:
            print('Вы не превышаете.')


class SportCar(Car):
    def show_speed(self):
        print(f'Текущая скорость  {self.name} составляет {self.speed}')
        if self.speed > 100:
            print('Вам пора на трек')
        else:
            print('Вы не превышаете.')


class WorkCar(Car):
    def show_speed(self):
        print(f'Текущая скорость  {self.name} составляет {self.speed}')
        if self.speed > 40:
            print('Вы превышаете!')
        else:
            print('Вы не превышаете.')


class PoliceCar(Car):
    def police(self):
        if self.is_police:
            print(f' {self.name} - машина спецслужб')
        else:
            print(f' {self.name} - обычная машина')


Car_for_police = PoliceCar()

Car_for_work = WorkCar()
Car_for_work.go()
Car_for_work.turn_left()
Car_for_work.turn_right()
Car_for_work.show_speed()
Car_for_work.stop()

Car_for_city = TownCar()
Car_for_work.go()
Car_for_city.show_speed()
Car_for_city.stop()

"""
Задание 5.
Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем публичный атрибут title (название) и публичный метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса: Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self):
        self.title = input('Задайте название')
        self.color = input('Задайте цвет')

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f' Ух ты! какой красивый тонкий рисунок {self.title} ручкой! А это какой цвет, {self.color}? Здорово!')


class Pencil(Stationery):
    def draw(self):
        print(f'Ничего себе! Ты так красиво рисуешь карандашом {self.title}! И ты здорово выбрал {self.color} цвет!')


class Handle(Stationery):
    def draw(self):
        print(
            f'Вау! Маркером получился очень яркий рисунок {self.title}! Кстати,самый лучший цвет для него {self.color}, но, я вижу, ты и так это знаешь!')


pen_draw = Pen()
pen_draw.draw()

pencil_draw = Pencil()
pencil_draw.draw()

handle_draw = Handle()
handle_draw.draw()
