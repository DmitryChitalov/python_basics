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

6. Продолжить работу над пятым заданием. Р
еализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров,
отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте
«Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""

class OfficeDevices:

    dev_type = 'device'

    def __init__(self, brand, model_code, price, weight, quantity, manu_date):
        try:
            self.brand = brand
            self.model_code = model_code
            self.price = float(price)
            self.weight = float(weight)
            self.manu_date = manu_date
            self.dev_qantity = int(quantity)
            self.dev_info = {'Device_brand': self.brand, 'Device_type': self.dev_type,
                         'Device_model': self.model_code, 'Unit_price': self.price,
                         'Unit_weight_(kg)': self.weight, 'Qantity of units': self.dev_qantity,
                         'Manufacture_date': self.manu_date}
        except ValueError:
            print(
                f'Ошибка во введенном значении. Сведения для {self.brand} {self.dev_type} не сохранены.')

    def __str__(self):
        return f'Device info: {self.dev_info}'

    def __call__(self):
        return self.dev_info


class Printer(OfficeDevices):

    dev_type = 'printer'

class Scanner(OfficeDevices):

    dev_type = 'scanner'

class MultiFuncUnit(OfficeDevices):

    dev_type = 'MFU'

class OfficeDeviceStorage:

    def __init__(self, storage_items):
        self.storage_items = [storage_items]

    def add_to_storage(self, dev_info):
        self.storage_items.append(dev_info)

    def take_on_storage(self):
        while True:
            try:
                dev_brand = input('Device manufacturer (brand): ')
                dev_type = input('Type of device: ')
                dev_model = input('Model number or codename: ')
                dev_price = float(input('Device unit price: '))
                dev_weight = float(input('Device weight (kg): '))
                dev_quantity = int(input('Units quantity: '))
                dev_mandate = input('Device manufacture date (year): ')

                new_dev_info = {'Device_brand': dev_brand, 'Device_type': dev_type,
                                'Device_model': dev_model, 'Unit_price': dev_price,
                                'Unit_weight_(kg)': dev_weight, 'Quantity of units': dev_quantity,
                                'Manufacture_date': dev_mandate}

                self.storage_items.append(new_dev_info)

                nonstop = input(
                    'Take on storage one more item: Y(enter)/n: ').lower()
                if nonstop == 'n':
                    break
            except ValueError:
                print('Введено недопустимое значение. Добавление на склад прервано.')
                break

fin_printer = Printer('Samsung', 3200, 10000, 5, 'two', 2019)
hr_printer = Printer('Samsung', 3200, 10000, 5, 3, 2019)
des_scanner = Scanner('HP', '2833i', 15000, 3, 1, 2021)
sec_mfu = MultiFuncUnit('Canon', 'T1000', 250000, 25, 1, 2015)
empty_store = {'Dev': 'nothing'}

"""
Ниже представлено несколько различных способов передачи существующих девайсов на склад.
Склад представляет собой список словарей с информацией о хранимом девайсе
"""
empty_warehouse = OfficeDeviceStorage(empty_store)

first_warehouse = OfficeDeviceStorage(hr_printer.dev_info)

first_warehouse.add_to_storage(des_scanner.dev_info)

first_warehouse.add_to_storage(sec_mfu())

first_warehouse.take_on_storage()

"""
В зависимости от удобства пользования метод OfficeDeviceStorage.take_on_storage()
можно исключить из класса "Склад" и с небольшими изменениями перенести код 
в конструктор класса "Оргтехника",чтобы ввод информации о девайсе был более наглядным
и понятным для пользователя.А программа в таком случае избавляется от 
дублирования кода словаря девайса в классе "Склад".
"""
print(empty_warehouse.storage_items)
print(first_warehouse.storage_items)
