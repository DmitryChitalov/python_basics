"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над четвертым заданием.
Разработать методы, отвечающие за приём оргтехники на
склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и
количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над пятым заданием.
Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров,
отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте
«Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""

# Выводим на экран задание
print('\nУрок 8 Задание 3\n')

# Создаем класс для ловли исключений
class MyExpDig(Exception):

    def __set__(self, instance, value):
        try:
            value = float(value)
        except:
            print('Значение должно быть числом')
        else:
            instance.__dict__[self.my_attr] = value


    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr

# Создаём родительский класс
class OficeEquipment:
    quantity = MyExpDig()
    coast = MyExpDig()

    def __init__(self, input_dev):
        temp_list = input_dev.split()
        self.name = temp_list[0]
        self.quantity = temp_list[1]
        self.coast = temp_list[2]
        self.place = temp_list[3]
        self.dict = {'Название': self.name, 'Количество': self.quantity,
                     'Цена за еденицу': self.coast, 'Расположение': self.place}

    def __str__(self):
        return f'{self.dict}'

# Создаем класс принтер
class Printer(OficeEquipment):
    pass

# Создаем класс сканер
class Scaner(OficeEquipment):
    pass

# Создаем класс МФУ
class MFD(OficeEquipment):
    pass

# Создаем класс склада
class StoreDiv:
    devices: [OficeEquipment]

    def __init__(self):
        self.devices = []

    def add_devices(self, in_dev: OficeEquipment):
        self.devices.append(in_dev)

    def get_device(self, pos):
        return self.devices[pos-1]

    def rem_devices(self, pos):
        self.devices.pop(pos-1)

    def __str__(self):
        for i in range(0, len(self.devices)):
            print(f'Номер по порядку: {i+1}.\n'
                  f'Устройство: {self.devices[i]}')
        return ''

# Определяем переменные
printer_1 = Printer('Принтер1 1 100 15B')
scaner_1 = Scaner('Сканер1 2 200 15A')
multi_1 = MFD('МФУ1 1 300 25D')
printer_2 = Printer('Принтер2 3 100 11B')
scaner_2 = Scaner('Сканер2 3 200 12A')
multi_2 = MFD('МФУ2 3 300 23D')

print(f'Исходный список устройств:\n'
      f'{printer_1}\n'
      f'{printer_2}\n'
      f'{scaner_1}\n'
      f'{scaner_2}\n'
      f'{multi_1}\n'
      f'{multi_2}')

# Объявляем склады
store_1 = StoreDiv()
store_2 = StoreDiv()

# Наполняем склады
store_1.add_devices(printer_1)
store_2.add_devices(printer_2)
store_1.add_devices(scaner_1)
store_1.add_devices(scaner_2)
store_1.add_devices(multi_1)
store_2.add_devices(multi_2)
print(f'Содержимое первого склада:')
print(f'{store_1}')
print()
print(f'Содержимое второго склада:')
print(f'{store_2}')
print()

# Перемещаем технику между складами
print(f'Перемещение позиции №3 из первого склада  во второй')
position_change = 3
store_2.add_devices(store_1.get_device(3))
store_1.rem_devices(position_change)

# Выводим содержимое складов
print(f'Содержимое первого склада:')
print(f'{store_1}')
print()
print(f'Содержимое второго склада:')
print(f'{store_2}')
