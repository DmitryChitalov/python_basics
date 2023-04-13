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
import copy
import json


class TechnicTypeNotFoundError(Exception):
    def __init__(self, type_name):
        self.message = f"{type_name}s not found"
        super().__init__(self.message)


class TechnicNotFoundError(Exception):
    def __init__(self):
        self.message = f"Free technic not found on storage"
        super().__init__(self.message)


class Storage:
    __items = {}

    @property
    def items(self):
        return self.__items

    def __init__(self):
        pass

    def add(self, tech_object, count=1):
        key = tech_object.__class__.__name__
        for i in range(count):
            if key in self.__items.keys():
                self.__items[key].append(copy.copy(tech_object))
            else:
                self.__items[key] = [tech_object]

    def move(self, tech_object, department):
        key = tech_object.__class__.__name__

        if key not in self.__items.keys():
            raise TechnicTypeNotFoundError(key)

        for idx, item in enumerate(self.__items[key]):
            if item.department == '':
                self.__items[key][idx].department = department
                return

        raise TechnicNotFoundError()

    def get_items(self, filter_flag='f'):
        if filter_flag == 'a':  # Full list
            return {key: len(arr) for key, arr in self.__items.items()}
        if filter_flag == 'f':  # Free items only
            return {key: len([x for x in arr if x.department == '']) for key, arr in self.__items.items() if
                    len([x for x in arr if x.department == '']) > 0}
        if filter_flag == 'd':
            deps = {}

            for tech_type in self.__items.keys():
                for tech in self.__items[tech_type]:
                    if tech.department not in deps.keys():
                        deps[tech.department] = {}
                    if tech_type not in deps[tech.department].keys():
                        deps[tech.department][tech_type] = 0
                    deps[tech.department][tech_type] += 1

            del deps['']
            return json.dumps(deps, indent=2)

        return {}


class Technic:
    department = ''

    def __init__(self):
        pass

    def get_name(self):
        return self.__class__.__name__

    @staticmethod
    def factory(object_code):
        if object_code not in Technic.get_tech_codes():
            return None

        if object_code == Scaner.TECH_CODE:
            return Scaner()
        elif object_code == Printer.TECH_CODE:
            return Printer()
        elif object_code == Xerox.TECH_CODE:
            return Xerox()

    @staticmethod
    def get_tech_codes():
        return [Printer.TECH_CODE, Scaner.TECH_CODE, Xerox.TECH_CODE]


class Printer(Technic):
    TECH_CODE = 'p'


class Scaner(Technic):
    TECH_CODE = 's'


class Xerox(Technic):
    TECH_CODE = 'x'


class UserShell:
    _storage = None

    def __init__(self):
        self._storage = Storage()
        pass

    def __request_command(self, prompt, to_lower=True):
        command = input(f"{prompt}: ").strip()
        return command.lower() if to_lower is True else command

    def __print_help(self):
        commands = {
            'Commands:': {
                's [flags]\t\t\t': 'Show free items in storage',
                '\t-a\t\t\t\t': 'Flag to show all items, including in departments',
                '\t-d\t\t\t\t': 'Flag to show items in departments',
                'add <count> <p,s,x>\t': 'Add [count] items of [p]rinter/[s]caner/[x]erox to storage',
                'move <p,s,x> <dptmt>': 'Move [p]rinter/[s]caner/[x]erox to [dptmt] departament',
                'q\t\t\t\t\t': 'Quit',
            },
            'Usage:': {
                's\t\t\t\t\t': 'Display all free items in storage',
                's -a\t\t\t\t': 'Display all items in storage, including with department',
                's -d\t\t\t\t': 'Display all items grouped by department',
                'add 3 p\t\t\t\t': 'Add 3 printers to storage',
                'move s Department 2\t': 'Move scaner to Department 2',
            }
        }
        for section, cmds in commands.items():
            print(section)
            for cmd, description in cmds.items():
                print(f"\t{cmd}\t{description}")

    def run(self):
        while True:
            command = self.__request_command("Type command ('h' for help)")
            if command == '':
                print('There is no command. Try agen.')
            elif command == 'q':  # Quit
                print("Application Quit")
                break
            elif command == 'h':  # Print help
                self.__print_help()
            else:
                action, *parameters = command.split(' ')
                if action not in ['a', 'm', 's', 'add']:
                    print('Undefined command')
                    continue

                if action in ['a', 'm', 'add']:
                    try:
                        tech_code = parameters[1]
                    except IndexError:
                        print(f"Technic code is not set")
                        continue

                    if tech_code not in Technic.get_tech_codes():
                        print('Technic is undefined')
                        continue

                    if action in ['a', 'add']:  # Add to storage
                        try:
                            count = int(parameters[0])
                        except ValueError:
                            print(f"{parameters[0]} is not positive integer value, greater than 0. Canceled.")
                            continue
                        self._storage.add(Technic.factory(tech_code), count)
                        print(f"{count} {Technic.factory(tech_code).get_name()}(s) added to storage")
                    elif action == 'm':  # Move to department
                        try:
                            department_name = ' '.join(parameters)
                            self._storage.move(Technic.factory(tech_code), department_name)
                            print(f"{Technic.factory(tech_code).get_name()} moved to {department_name}")
                        except TechnicTypeNotFoundError as ex:
                            print(ex.message)

                    continue

                if action in ['s']:
                    if len(parameters) == 0:
                        print(self._storage.get_items('f'))
                    else:
                        if parameters[0] not in ['-f', '-d']:
                            print(f"Flag {parameters[0]} is undefined")
                            continue
                        if parameters[0] == '-a':
                            print(self._storage.get_items('a'))
                        if parameters[0] == '-d':
                            print(self._storage.get_items('d'))


# storage = Storage()
#
# scaner1 = Scaner()
# scaner2 = Scaner()
# scaner3 = Scaner()
#
# printer1 = Printer()
# printer2 = Printer()
#
# xerox1 = Xerox()
#
# storage.add(scaner1)
# storage.add(scaner2)
# storage.add(scaner3)
#
# storage.add(printer1)
# storage.add(printer2)
#
# storage.add(xerox1)
#
# storage.move(xerox1, 'Dep 1')
# storage.move(scaner1, 'Dep 2')
# storage.move(printer2, 'Dep 2')

shell = UserShell()
shell.run()
