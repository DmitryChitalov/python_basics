#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Задание 1. Создать класс TrafficLight (светофор).
#определить у него один атрибут color (цвет) и метод running (запуск);
#атрибут реализовать как приватный;
#в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
#продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше
#усмотрение;переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
#проверить работу примера, создав экземпляр и вызвав описанный метод.Проверить работу примера, создав экземпляр и вызвав 
#описанный метод.

from time import sleep

class TrafficLight:
    __color = {'Красный': 7, 'Желтый': 2, 'Зеленый': 4}

    @staticmethod
    def running() -> None:
        for key, value in TrafficLight.__color.items():
            print(f'Сейчас горит цвет: {key}')
            sleep(value)
            print(f'Переключаю цвет светофора')


if __name__ == '__main__':
    TrafficLight.running()


# In[ ]:


#Задание 2. Реализовать класс Road (дорога).
#определить атрибуты: length (длина), width (ширина);
#значения атрибутов должны передаваться при создании экземпляра класса;
#атрибуты сделать защищёнными;
#определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
#использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см*число см 
#толщины полотна;проверить работу метода.
#Например: 20 м*5000 м*25 кг*5 см = 12500 т.
    
class Road:
    weight = 25
    height = 0.05

    def __init__(self, width, length):
        self._width = width
        self._length = length


    def asphalt_mass(self):
        asphalt_mass = self._length * self._width * Road.weight * Road.height / 1000
        print(f'Необходимо {round(asphalt_mass)} тонн асфальта')


r = Road(20, 5000)
r.asphalt_mass()


# In[ ]:


#Задание 3. Реализовать базовый класс Worker (работник).
#определить атрибуты: name, surname, position (должность), income (доход);
#последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например, 
#{"wage": wage, "bonus": bonus};создать класс Position (должность) на базе класса Worker;
#в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии 
#(get_total_income);проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, 
#проверить значения атрибутов, вызвать методы экземпляров.

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": int(wage), "bonus": int(bonus)}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


p = Position('Иван', 'Иванов', 'IT', '80000', '20000')
print(p.get_full_name(), p.get_total_income())


# In[ ]:


#Задание 4. Реализуйте базовый класс Car.
#у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), 
#которые должны сообщать, что машина поехала, остановилась, повернула (куда);опишите несколько дочерних классов: TownCar, 
#SportCar, WorkCar, PoliceCar;добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
#для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно 
#выводиться сообщение о превышении скорости.


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.color} {self.name} поехала.")

    def stop(self):
        print(f"{self.color} {self.name} остановилась.")

    def turn(self, direction):
        print(f"{self.color} {self.name} повернула {direction}.")

    def show_speed(self):
        print(f"Текущая скорость {self.color} {self.name}: {self.speed} км/ч.")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"{self.color} {self.name} превысила скорость!")
        else:
            print(f"Текущая скорость {self.color} {self.name}: {self.speed} км/ч.")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"{self.color} {self.name} превысила скорость!")
        else:
            print(f"Текущая скорость {self.color} {self.name}: {self.speed} км/ч.")


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=True)


car1 = TownCar(70, "черная", "Городская машина")
car2 = SportCar(120, "красная", "Спортивная машина")
car3 = WorkCar(30, "серая", "Рабочая машина")
car4 = PoliceCar(90, "сине-белая", "Полицейская машина")

print(car1.speed, car1.color, car1.name, car1.is_police)
print(car2.speed, car2.color, car2.name, car2.is_police)
print(car3.speed, car3.color, car3.name, car3.is_police)
print(car4.speed, car4.color, car4.name, car4.is_police)

car1.go()
car1.turn("направо")
car1.show_speed()

car2.go()
car2.stop()
car2.show_speed()

car3.turn("налево")
car3.show_speed()

car4.go()
car4.show_speed()


# In[ ]:


#Задание 5. Реализовать класс Stationery (канцелярская принадлежность).
#определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
#создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
#в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
#создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки'


class Pen(Stationery):
    def draw(self):
        return f'Отрисовка {self.title}'


class Pencil(Stationery):
    def draw(self):
        return f'Отрисовка {self.title}'


class Handle(Stationery):
    def draw(self):
        return f'Отрисовка {self.title}'


pen = Pen('ручкой')
print(pen.draw())
pencil = Pencil('карандашем')
print(pencil.draw())
handle = Handle('маркером')
print(handle.draw())


# In[ ]:





# In[ ]:




