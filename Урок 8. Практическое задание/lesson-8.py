"""
Задание 1.

Реализовать класс «Дата», на уровне класса определить атрибут day_month_year,
присвоить ему значение

В рамках класса реализовать два метода.

Первый, с декоратором @classmethod, должен извлекать число, месяц,
год, преобразовывать их тип к типу «Число» и делать атрибутами класса.

Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Data:
    def __init__(self, day_month_year):
        self.day_month_year = day_month_year.split()

    @classmethod
    def get_data(cls, day_month_year):
        temp_list = []
        for i in day_month_year:
            if i != '-' and i != ':' and i != '.':
                temp_list.append(i)
        for i in temp_list:
            day = int(temp_list[0] + temp_list[1])
            month = int(temp_list[2] + temp_list[3])
            year = int(temp_list[4] + temp_list[5] + temp_list[6] + temp_list[7])
        print(f'Чиcло  {day}, месяц {month}, год {year}')
        Data.valid_data(day, month, year)

    @staticmethod
    def valid_data(day, month, year):
        if day >= 1 and day < 31:
            print("Число корректное")
        else:
            print("Вы ошиблись  с числом")
        if month >= 1 and month <= 12:
            print("Месяц корректный")
        else:
            print("Вы ошиблись  с месяцем")
        if year >= 1900 and year <= 2100:
            print("Год корректный")
        else:
            print("Возможно, вы путешественник во времени?")


Data.get_data(input('Введите дату'))

"""
Задание 2.
Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class myExceptions(Exception):
    def __init__(self, txt):
        self.txt = txt


divisible = int(input("Введите делимое"))
divider = int(input("Введите делитель"))
try:
    if divider == 0:
        raise myExceptions("Деление на 0 недопустимо")
    else:
        print(f"Результат деления {divisible / divider}")
except myEcxeptions as err:
    print(err)

"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""


class myException_list(Exception):
    def __init__(self, txt):
        self.txt = txt


ex_list = input("Введите список чисел через пробел ").split()
rezult_list = []
for i in ex_list:
    try:
        i = int(i)
    except ValueError:
        print(f"На позиции {ex_list.index(i)} Вы ввели не число")
    except OwnError as err:
        print(err)
    else:
        rezult_list.append(i)
print(rezult_list)

"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники."""

"""
5. Продолжить работу над четвертым заданием.
Разработать методы, отвечающие за приём оргтехники на
склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и
количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над пятым заданием. Р
еализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров,
отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте
«Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""


class Warehouse:
    def __init__(self):
        self.name = input("Введите имя склада")
        self.dist = input('Введите удаленность от административного центра')

    def sort_to_warehouse(self, ident):
        if ident == "printer":
            if printer_ob.color == True:
                print(f'Принтер {printer_ob.name} поедет на склад {wareh_1.name}')
            else:
                print(f'Принтер {printer_ob.name} поедет на склад {wareh_2.name}')
        elif ident == "scanner":
            if scanner_ob.size > 2:
                print(f'Сканнер {scanner_ob.name} поедет на склад {wareh_1.name}')
            else:
                print(f'Сканнер {scanner_ob.name} поедет на склад {wareh_2.name}')
        elif ident == "xerox":
            if xerox_ob.size > 100:
                print(f'Ксерокс {xerox_ob.name} поедет на склад {wareh_1.name}')
            else:
                print(f'Ксерокс {xerox_ob.name} поедет на склад {wareh_2.name}')
        else:
            print("укажите, отправление какого оборудования Вас интересует")


class Office_equipment(Warehouse):
    def __init__(self, name, cost, vendor, number):
        self.name = name
        self.cost = cost
        self.vendor = vendor
        self.number = number

    def get_number(self, number):
        print(f'Сейчас на складе {number} единиц оборудования')
        take_number = input("укажите, сколько единиц надо забрать")
        try:
            take_number = int(take_number)
        except ValueError:
            print(f"Вы ввели не число")
            return 0
        if number - take_number < 0:
            print("Оборудования не хватает. Заберите поменьше")
        else:
            print(f'Осталось {number - take_number} единиц оборудования')


class Scanner(Office_equipment):
    def __init__(self, name, cost, vendor, number, size):
        super().__init__(name, cost, vendor, number)
        self.size = size


class Printer(Office_equipment):
    def __init__(self, name, cost, vendor, number, color):
        super().__init__(name, cost, vendor, number)
        self.color = color


class Xerox(Office_equipment):
    def __init__(self, name, cost, vendor, number, speed):
        super().__init__(name, cost, vendor, number)
        self.speed = speed


wareh_1 = Warehouse()
wareh_2 = Warehouse()

printer_ob = Printer("Canon 150 MP", 200000, "Canon", 30, True)
scanner_ob = Scanner("HP-410 Tank", 200000, "HP", 30, 1.5)
xerox_ob = Scanner("Xerox Pro", 200000, "Xerox", 30, 200)

printer_ob.get_number(20)
scanner_ob.get_number(52)
xerox_ob.get_number(15)

printer_ob.sort_to_warehouse("printer")
scanner_ob.sort_to_warehouse("scanner")
xerox_ob.sort_to_warehouse("xerox")

"""
Задание 7.*

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата. (a+b)(c+d)=(ac-bd)+(bc+ad)i
"""


class Complex_number:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        self.sum_a = self.a + other.a
        self.sum_b = self.b + other.b
        return f'Сумма равняется {self.sum_a} + {self.sum_b}i'

    def __sub__(self, other):
        self.sum_a = self.a - other.a
        self.sum_b = self.b - other.b
        return f'Разность равняется {self.sum_a} + {self.sum_b}i'

    def __mul__(self, other):
        self.mul_a = self.a * other.a - self.b * other.b
        self.mul_b = self.b * other.a + self.a * other.b
        return f'Произведение равняется {self.mul_a} + {self.mul_b}i'


x = Complex_number(2, 4)
y = Complex_number(3, 5)

print(x + y)
print(x - y)
print(x * y)
