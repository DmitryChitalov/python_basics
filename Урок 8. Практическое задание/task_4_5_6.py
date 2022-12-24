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

### Блок Программы

class MyException(ValueError):
    '''Собственный класс исключения'''
    def __init__(self, txt):
        self.txt = txt


class Technics:
    """Базовый класс оргтехники"""
    list_all_tech = []
    list_tech = []
    dict_tech = {}
    list_transmit_tech = []
    dict_transmit_tech = {}

    def __init__(self, name, model):
        self.name = name
        self.model = model

    def __str__(self):
        return f"В баззу внесена техника фирмы: {self.name}. "\
            f"Модель: {self.model}"

    def get_tech_on_warehouse(self):
        """Базовый метод, определяющий прием техники на склад"""

        self.dict_tech = {
            'Название': self.name,
            'Модель': self.model,
        }
        self.list_tech.append(self.dict_tech)
        return self.dict_tech

    @staticmethod
    def transmit_to_office(office: str, number: int):
        """Метод передачи техники в офис"""

        new_tech_to_office = Technics.list_tech
        tech_to_office = Technics.list_tech[:number]

        dict_transmit_tech = {
            'Подразделение': office,
            'Количество': number,
            'Техника': tech_to_office
        }
        Technics.list_transmit_tech.append(dict_transmit_tech)

        for elem in tech_to_office:
            new_tech_to_office.pop(new_tech_to_office.index(elem))

        Technics.list_tech = new_tech_to_office

    @classmethod
    def all_technics(cls):
        """Метод учета техники"""
        return f"\nВсего числится техники: {cls.list_all_tech}\n\n"\
            f"На складе: {cls.list_tech}\n\n"\
                f"В офисах: {cls.list_transmit_tech}"

    @classmethod
    def get_info(cls, param):
        """
        Метод вывода информации
        -----------------------
        'склад' - остаток на складе
        'офисы' - какая техника в офисах
        """
        if param.lower() == 'склад':
            return cls.list_tech
        elif param.lower() == 'офисы':
            return cls.list_transmit_tech


class Printer(Technics):
    """
    Класс-наследник для принтеров
    -----------------------------
    Атрибуты при создании экземпляра:

    name - Название;
    model - Модель;
    trays - Кол-во лотков бумаги
    """

    def __init__(self, name, model, trays):
        super().__init__(name, model)
        self.trays = trays

    def get_tech_on_warehouse(self):
        """Метод, определяющий прием техники на склад"""

        self.dict_tech = {
            'Принтер': {
                'Название': self.name,
                'Модель': self.model
            }
        }
        self.list_tech.append(self.dict_tech)
        self.list_all_tech.append(self.dict_tech)
        return self.dict_tech

    @classmethod
    def all_technics(cls):
        """Метод ведения склада"""
        printers_lst = []
        for printers in cls.list_tech:
            for printer in printers:
                if printer == 'Принтер':
                    printers_lst.append(printers[printer])
        return f"Числится принтеров: {printers_lst}"


class Scaner(Technics):
    """
    Класс-наследник для сканеров
    -----------------------------
    Атрибуты при создании экземпляра:

    name - Название;
    model - Модель;
    parts - Кол-во интерфейсов для сканирования
    """

    def __init__(self, name, model, parts):
        super().__init__(name, model)
        self.parts = parts

    def get_tech_on_warehouse(self):
        """Метод, определяющий прием техники на склад"""

        self.dict_tech = {
            'Сканер': {
                'Название': self.name,
                'Модель': self.model
            }
        }
        self.list_tech.append(self.dict_tech)
        self.list_all_tech.append(self.dict_tech)
        return self.dict_tech

    @classmethod
    def all_technics(cls):
        """Метод ведения склада"""
        scaners_lst = []
        for scaners in cls.list_tech:
            for scaner in scaners:
                if scaner == 'Сканер':
                    scaners_lst.append(scaners[scaner])
        return f"Числится сканеров: {scaners_lst}"


class Copier(Technics):
    """
    Класс-наследник для копировальных машин
    -----------------------------
    Атрибуты при создании экземпляра:

    name - Название;
    model - Модель;
    send_email - Наличие функции отправки Email
    """

    def __init__(self, name, model, send_email: bool):
        super().__init__(name, model)
        if send_email:
            self.send_email = "С функцией отправки по Email"
        else:
            self.send_email = "Без функции отправки по Email"

    def get_tech_on_warehouse(self):
        """Метод, определяющий прием техники на склад"""

        self.dict_tech = {
            'Копировальная машина': {
                'Название': self.name,
                'Модель': self.model
            }
        }
        self.list_tech.append(self.dict_tech)
        self.list_all_tech.append(self.dict_tech)
        return self.dict_tech

    @classmethod
    def all_technics(cls):
        """Метод ведения склада"""
        copiers_lst = []
        for copiers in cls.list_tech:
            for copier in copiers:
                if copier == 'Копировальная машина':
                    copiers_lst.append(copiers[copier])
        return f"Числится копировальных машин: {copiers_lst}"


### Блок клиентской программы

def check_error(user_ent):
    """Функция проверки вводимых данных в меню"""

    try:
        if user_ent.isdigit():
            int(user_ent)
        else:
            raise MyException("Вы вводите не число! Нужно ввести только число!")
    except MyException as err:
        print(err)
    else:
        print("\nИтак, далее...\n")
        return True


def add_technics_in_sys(param):
    """
    Функция ползовательского ввода данных о видах техники
    -----------------------------------------------------
    Дополнительные переменные:

    1 - Принтер;
    2 - Сканер;
    3 - Копировальная машина
    """

    name = input("Введите наименование бренда: ")
    model = input("Введите модель: ")

    if param == '1':
        tray = int(input("Введите количество лотков для бумаги: "))
        return name, model, tray
    elif param == '2':
        parts = int(input("Введите количество сторон для сканирования: "))
        return name, model, parts
    elif param == '3':
        send_email = input("Имеется ли возможность отправлять копии по Email (True/False): ")
        return name, model, send_email


print('Добро пожаловать в программу 5-Зет "Ведение учета"')
while True:
    print("""\nВыберите один из следующих вариантов:
    1 - вывести информацию о наличии техники на учете)
    2 - вывести информацию о техники на складе или в других офисах
    3 - вывести данные о технике
    4 - заполнить карточку учета с данными о технике
    5 - осуществить передачу техники в офисы
    Если вы хотите закончить - введите 'закончить работу'\n
    """)
    user_ent = input('Введите число: ')
    if user_ent.isdigit() and int(user_ent) > 5:
        print("\nВнимательно смотрите на меню! "\
                            "Выбрать можно только один из трех вариантов.\n")
    else:
        if user_ent.lower() == 'закончить работу':
            break
        if check_error(user_ent):
            if int(user_ent) == 1:
                print(Technics.all_technics())
            elif int(user_ent) == 2:
                print('Введите дополнительный параметр "офисы" или "склад":')
                dif_user = input()
                if dif_user.lower() == 'офисы':
                    if len(Technics.get_info(param=dif_user)) == 0:
                        print("В офисах сейчас техника не числится")
                    else:
                        print("В офисах сейчас следующая техника:")
                        for el in Technics.get_info(param=dif_user):
                            print(el)
                elif dif_user.lower() == 'склад':
                    if len(Technics.get_info(param=dif_user)) == 0:
                        print("На складе сейчас нет техники")
                    else:
                        print(f"На складе сейчас {len(Technics.get_info(param=dif_user))} ед.:")
                        for el in Technics.get_info(param=dif_user):
                            print(el)
                else:
                    print("\nПожалуйста в следующий раз проверьте ввод.\n")
            elif int(user_ent) == 3:
                while True:
                    print("""\nВыберите один из следующих вариантов:
                    1 - вывести информацию о принтерах
                    2 - вывести информацию о сканерах
                    3 - вывести информацию о копирах
                    Если вы хотите закончить - введите 'закончить просмотр'\n
                    """)
                    user_ent = input('Введите число: ')
                    if user_ent.isdigit() and int(user_ent) > 3:
                        print("\nВнимательно смотрите на меню! "\
                            "Выбрать можно только один из трех вариантов.\n")
                    else:
                        if user_ent.lower() == 'закончить просмотр':
                            break
                        if check_error(user_ent):
                            if int(user_ent) == 1:
                                print(Printer.all_technics())
                            elif int(user_ent) == 2:
                                print(Scaner.all_technics())
                            elif int(user_ent) == 3:
                                print(Copier.all_technics())
                            else:
                                print("\nПожалуйста в следующий раз проверьте ввод.\n")
            elif int(user_ent) == 4:
                while True:
                    print("""\nВыберите один из следующих вариантов:
                    1 - ввести информацию о принтере
                    2 - ввести информацию о сканере
                    3 - ввести информацию о копире
                    Если вы хотите закончить - введите 'закончить ввод'\n
                    """)
                    user_ent = input('Введите число: ')
                    if user_ent.isdigit() and int(user_ent) > 3:
                        print("\nВнимательно смотрите на меню! "\
                            "Выбрать можно только один из трех вариантов.\n")
                    else:
                        if user_ent.lower() == 'закончить ввод':
                            break
                        if check_error(user_ent):
                            if int(user_ent) == 1:
                                tech_in = add_technics_in_sys('1')
                                printer = Printer(name=tech_in[0], model=tech_in[1],
                                    trays=tech_in[2])
                                printer.get_tech_on_warehouse()
                                print(f"\n{printer}\n")
                            elif int(user_ent) == 2:
                                tech_in = add_technics_in_sys('2')
                                scaner = Scaner(name=tech_in[0], model=tech_in[1],
                                    parts=tech_in[2])
                                scaner.get_tech_on_warehouse()
                                print(f"\n{scaner}\n")
                            elif int(user_ent) == 3:
                                tech_in = add_technics_in_sys('3')
                                copier = Copier(name=tech_in[0], model=tech_in[1],
                                    send_email=tech_in[2])
                                copier.get_tech_on_warehouse()
                                print(f"\n{copier}\n")
                            else:
                                print("\nПожалуйста в следующий раз проверьте ввод.\n")

            elif int(user_ent) == 5:
                print('\nСистема распределения техники:\n')
                if len(Technics.list_tech) == 0:
                    print("На складе нет техники, чтобы ее передать!")
                else:
                    print("Кажется что-то завалялось...\n")
                    user_ent = input("Введите кол-во техники, планируемое к передаче: ")
                    if check_error(user_ent):
                        if int(user_ent) > len(Technics.list_tech):
                            print("\nНа складе нет столько техники.")
                            print(f"Сейчас на складе {len(Technics.list_tech)} ед. техники.\n")
                        else:
                            print("\nВведите название офиса:")
                            office = input()
                            Technics.transmit_to_office(office=office, number=int(user_ent))
                    else:
                        print("\nПожалуйста в следующий раз проверьте ввод.\n")


print("\nМы закончили. Отлично поработали!!!\n")
print(Technics.all_technics())
