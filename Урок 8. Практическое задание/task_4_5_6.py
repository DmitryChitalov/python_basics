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


class Warehouse:
    wh_status = {}

    @classmethod
    def get_available_qtty(cls, model):
        # Проверка корректности модели в заявке
        if not model in cls.wh_status.keys():
            print('Указанная модель отсутствует на складе')
            return 0
        else:
            return cls.wh_status.get(model).get('warehouse_qtty')

    @classmethod
    def to_site_office(cls, model, qtty):
        #Проверка наличного количества:
        try:
            if cls.get_available_qtty(model) >= int(qtty) and int(qtty)>=0:
                wh_qtty = cls.get_available_qtty(model)
                site_qtty = cls.wh_status.get(model).get('site_office_qtty')
                cls.wh_status.get(model).update({'warehouse_qtty': wh_qtty - qtty, 'site_office_qtty': site_qtty + qtty })
            else:
                print('Заявленное количество отсутствует на складе')
        except ValueError:
            print('Задайте количество целым числом')

    @classmethod
    def to_project_office(cls, model, qtty):
        try:
            # Проверка наличного количества:
            if cls.get_available_qtty(model) >= int(qtty) and int(qtty)>=0:
                wh_qtty = cls.get_available_qtty(model)
                proj_qtty = cls.wh_status.get(model).get('project_office_qtty')
                cls.wh_status.get(model).update({'warehouse_qtty': wh_qtty - qtty, 'project_office_qtty': proj_qtty + qtty})
            else:
                print('Заявленное количество отсутствует на складе')
        except ValueError:
            print('Задайте количество целым числом')


class OfficeEquipment:

    weight = None

    def __init__(self, model, *weight):
        self.model = model
        self.weight = weight

    # Отправка техники на склад
    def send_to_warehouse(self, qtty):
        if not self.model in Warehouse.wh_status.keys():
        #Если такой модели нет на складе,создать новую позицию
            try:
                Warehouse.wh_status.update({
                    self.model:
                    {
                        'warehouse_qtty': int(qtty),
                        'site_office_qtty': 0,
                        'project_office_qtty': 0
                    }
                })
            except ValueError:
                print('Задайте количество целым числом')

        #Если модель имеется, добавить соответствующее количество на склад
        else:
            old_qtty = Warehouse.get_available_qtty(self.model)
            Warehouse.wh_status.get(self.model).update({'warehouse_qtty': old_qtty+qtty})


class Printer(OfficeEquipment):

    def __init__(self, print_type, is_color, model, weight):
        super().__init__(model, weight)
        self.print_type = print_type
        self.is_color = is_color

class Scanner(OfficeEquipment):
    def __init__(self, scan_type, output_interface):
        self.scan_type = scan_type
        self.output_interface = output_interface


class Copier(OfficeEquipment):
    def __init__(self, is_color, copy_speed):
        self.is_color = is_color
        self.copy_speed = copy_speed


printer_1 = Printer('Лазерный', True, 'Super HP', 10)
#Получить наименование модели экземпляра 1
print(printer_1.model)
#Добавить партию 1
printer_1.send_to_warehouse(10)
#Статус 1
print(Warehouse.wh_status)
#Добавить партию 2
printer_1.send_to_warehouse(20)
#Статус 2
print(Warehouse.wh_status)
#Передать на площадку
Warehouse.to_site_office(printer_1.model, 9)
#Статус 3
print(Warehouse.wh_status)
#Передать в проектный офис
Warehouse.to_project_office(printer_1.model, 15)
#Статус 4
print(Warehouse.wh_status)



