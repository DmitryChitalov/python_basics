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

from task_4_5_6_classes.stock import Stock
from task_4_5_6_classes.printer import Printer
from task_4_5_6_classes.scanner import Scanner
from task_4_5_6_classes.xerox import Xerox
from task_4_5_6_classes.empty_list_error import EmptyListError

stock = Stock()
stock.add_item(Printer(1000, True))
stock.add_item(Printer(2000, True))
stock.add_item(Printer(2000, False))
stock.add_item(Xerox(3000, True))
stock.add_item(Scanner(5000, 1980, 1080))

printers = stock.get_items(Printer, 2)

try:
    scanners = stock.get_items(Scanner, 5)
except EmptyListError as error:
    print(error)

try:
    any_office_equipments = stock.get_items(int, 40)
except EmptyListError as error:
    print(error)