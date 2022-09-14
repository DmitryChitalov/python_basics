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


# статус оргтехники (неизвестен, не принята на склад, на складе, передана в подразделеие, списана)
storage_state = {'unknown': 0, 'not_in_store': 1, 'stored': 2, 'passed': 3, 'retired': 4}

# строки отображения статуса оргтехнки (в порядке их нумерации в storage_state)
storage_str = ('неизвестно', 'не на складе', 'на складе', 'передан в эксплуатацию', 'списан')

tech_name = {'printer': 'принтер', 'mfc': 'МФУ', 'scanner': 'сканер'}


class NotEmpty:

    def __init__(self, my_attr):
        self.my_attr = my_attr

    """ def __get__(self, instance, owner):
        return instance.__dict__[self.my_attr]"""

    def __set__(self, instance, value):
        if value != '':
            instance.__dict__[self.my_attr] = value
            return
        raise ValueError("Значение атрибута не может быть пустым!")

    """def __delete__(self, instance):
        del instance.__dict__[self.my_attr]"""

    def __str__(self):
        return str(self.my_attr)
class Orgtechnic:
    type = ''  # тип оргтехники (printer, mfc, scanner)

    def __init__(self, params, state=storage_state['unknown']):
        self.state = state
        self.params = {'manufacturer': params['manufacturer'],
                       'model': params['model'],
                       'interfaces': params['interfaces']
                       }

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        # print(f"value={value}") #debug
        if value not in storage_state.values():
            raise ValueError("Неверный параметр state")
        self._state = value

    def __str__(self):
        return f"Тип оргтехники: {tech_name[self.type]}\n" \
               f"Производитель: {self.params['manufacturer']}\n" \
               f"Модель: {self.params['model']}\n" \
               f"Интерфейсы: {self.params['interfaces']}\n " \
               f"Состояние: {storage_str[self.state]}"

    @classmethod
    def ask_new(cls):
        """
        Запрашивает у пользователя общие параметры оргтехники.
        :return: Производитель оргтехники, модель оргтехники
        """
        prm = {'manufacturer': input("Производитель: "), 'model': input("Модель: "),
               'interfaces': input("Интерфейсы: ")}
        print(f"prm = {prm}")  # debug
        return prm


class Printer(Orgtechnic):
    type: str = 'printer'

    def __init__(self, params, state=storage_state['unknown']):
        super().__init__(params, state)
        try:
            self.params.update({'paper_types': params['paper_types'],
                                'cartridge_types': params['cartridge_types']
                                })
        except KeyError:
            print("Недостаточно параметров для создания объекта \"Принтер\"")
            exit(1)

    def __str__(self):
        return f"Тип оргтехники: {tech_name[self.type]}\n" \
               f"Производитель: {self.params['manufacturer']}\n" \
               f"Модель: {self.params['model']}\n" \
               f"Интерфейсы: {self.params['interfaces']}\n " \
               f"Типы бумаги: {self.params['paper_types']}\n" \
               f"Типы картриджей: {self.params['cartridge_types']}\n" \
               f"Состояние: {storage_str[self.state]}"

    @classmethod
    def ask_new(cls):
        """
        Запрашивает у пользователя дополнительне параметры характерные для принтера
        :return: Производитель оргтехники, модель оргтехники, типы бумаги, типы картриджей, названия интерфейсов
        """
        prm = Orgtechnic.ask_new()
        prm.update({'paper_types': input("Формат бумаги: "), 'cartridge_types': input("Типы картриджей: ")})
        return prm


class Scanner(Orgtechnic):
    type = 'scanner'

    def __init__(self, params, state=storage_state['unknown']):
        super().__init__(params, state)
        try:
            self.params.update({'scanner_format': params['scanner_format'],
                                'scanner_type': params['scanner_type']
                                })
            if params['scanner_capacity'] <= 0:
                raise ValueError("Значение емкости лотка сканера должно быть больше нуля!")
            else:
                self.params.update({'scanner_capacity': params['scanner_capacity']})
        except KeyError:
            print("Недостаточно параметров для создания объекта \"Сканер\"")
            exit(1)

    def __str__(self):
        return f"{super().__str__()}\n" \
               f"Формат сканера: {self.params['scanner_format']}\n" \
               f"Тип сканера: {self.params['scanner_type']}\n" \
               f"Емкость лотка сканера: {self.params['scanner_capacity']}\n" \
               f"Состояние: {storage_str[self.state]}"

    @classmethod
    def ask_new(cls, part=False, prm={}):
        """
        Запрашивает у пользователя дополнительне параметры сканера.
        :param prm: опционально - словарь прочих параметров
        :param part - False - запрашивает общие для оргтехники параметры,
                    True - запрашивает только специфичные для сканера параметры. При этом общие параметры отдает
                    пустые значения
        :return: производитель, модель, интерфейсы, тип сканера, емкость лотка сканера, формат сканера
        """

        if not part:
            prm = Orgtechnic.ask_new()
        prm['scanner_type'] = input("Тип сканера (планшетный, потоковый, двусторонний и т.п.): ")
        prm['scanner_capacity'] = int(input("Емкость сканера (листов): "))
        prm['scanner_format'] = input("Формат сканирования: ")
        return prm


class Mfc(Printer):
    type = 'mfc'

    def __init__(self, params, state=storage_state['unknown']):
        super().__init__(params, state)
        try:
            self.params.update({'scanner_type': params['scanner_type'],
                                'scanner_format': params['scanner_format']
                                })
            if params['scanner_capacity'] <= 0:
                raise ValueError("Значение емкости лотка сканера должно быть больше нуля!")
            else:
                self.params.update({'scanner_capacity': params['scanner_capacity']})
        except KeyError:
            print("Недостаточно параметров для создания объекта \"МФУ\"")
            exit(1)

    def __str__(self):
        return f"{super().__str__()}\n" \
               f"Формат сканера: {self.params['scanner_format']}\n" \
               f"Тип сканера: {self.params['scanner_type']}\n" \
               f"Емкость лотка сканера: {self.params['scanner_capacity']}\n" \
               f"Состояние: {storage_str[self.state]}"

    @classmethod
    def ask_new(cls, prm={}):
        """
        Запрашивает у пользователя дополнительне параметры МФУ
        :return: производитель, модель, интерфейсы, форматы бумаги принтера, типы картриджей,
        тип сканера, емкость лотка сканера, формат сканера
        """
        prm = Printer.ask_new()
        prm.update(Scanner.ask_new(part=True))
        return prm


class Store:
    # id = 0
    city = NotEmpty('city')
    address = NotEmpty('address')
    items = []  # единицы хранения на складе

    def __init__(self, id, city, address):
        self.id = id
        self.city = city
        self.address = address

        print(f"Создан склад с параметрами: ID={self.id}, город {self.city}, адрес {self.address}")

    def __iter__(self):
        return iter(self.items)

    def add_tech_to_store(self, tech):
        """
        Добавление техники на склад.
        :param tech: Orgtechnic объект "оргтехника"
        :return: True - False -
        """
        print(type(tech))  # debug

        # tech.state = storage_state['stored']
        self.items.append(tech)
        print(f"Добавлена на склад техника: "
              f"{tech_name[tech.type]} "
              f"{tech.params['manufacturer']} "
              f"{tech.params['model']}"
              )

    def __str__(self):
        return f"Склад № {self.id}, город {self.city}, адрес: {self.address}."


def push_to_store_dlg():  # диалог добавление на склад
    print("Введите вид передаваемой на склад оргтехники:")
    print("1. Принтер")
    print("2. МФУ")
    print("3. Сканер")
    print("0. В главное меню")
    try:
        ch = int(input("Введите номер пункта меню: "))
    except ValueError:
        print("Неверный ввод!")
    else:
        if ch == 1:

            st.items.append(Printer(Printer.ask_new()))
        elif ch == 2:
            st.items.append(Mfc(Mfc.ask_new()))
        elif ch == 3:
            st.items.append(Scanner(Scanner.ask_new()))
        else:
            print("Возврат в главное меню.")
            return
        st.items[-1].state = storage_state['stored']
        print("Завершено добавление позиции на склад")
    return


def get_store_list_dlg(s: Store):
    print(s)
    print("\nОргтехника на складе:")

    i = 1
    for el in st:
        print(f"Поз.№{i}: {el}")
        i += 1
    return


def pass_to_department_dlg():
    """
    передача оргтехники в подразделение
    :return:
    """
    pos = 0
    while pos < 1 or len(st.items) < pos:
        pos = int(input("Введите номер позиции для передачи в эксплуатацию: "))
        if pos < 1 or len(st.items) < pos:
            print("Введен номер вне диапазона. ")
        else:
            break
    st.items[pos - 1].state = storage_state['passed']
    return


def show_main_menu(with_title=True):
    if with_title:
        print("\nГлавное меню программы")
    print("1. Прием техники на склад;")
    print("2. Просмотр списка техники на складе и в эксплуатации")
    print("3. Передача техники в эксплуатацию")
    print("0. Выход из программы")
    return


# ============== main code ======================
print("Введите данные склада:")
city = input("Город расположения: ")
addr = input("Адрес: ")

st = Store(12, city, addr)
print(st)

while True:  # main loop
    show_main_menu()
    try:
        choice = int(input("Введите номер пункта меню: "))
    except ValueError:
        print("Неверный ввод!")
    else:
        if choice == 1:
            push_to_store_dlg()
        elif choice == 2:
            get_store_list_dlg(st)
        elif choice == 3:
            get_store_list_dlg(st)
            pass_to_department_dlg()
        elif choice == 0:
            break
        else:
            print("Введите цифры 1, 2, 3, 0")
print("Работа программы завершена. Выход.")
