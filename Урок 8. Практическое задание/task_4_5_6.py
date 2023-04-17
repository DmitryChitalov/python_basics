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
class OfficeEquipment:

    def __init__(self, brand, model, price, quantity, number_of_lists, *args):
        self.brand = brand
        self.model = model
        self.price = price
        self.quantity = quantity
        self.number_of_lists = number_of_lists
        self.list_office_equipment  = []
    
    def __str__(self):
        return f' Производитель: {self.brand}\n Модель: {self.model}\n Цена: {self.price}\n Количество: {self.quantity}\n Заявленный объем работ (в листах): {self.number_of_lists}\n '

    def acceptance(self):
        while True:
            try:
                brand_eq = input(f'Введите марку оргтехники ')
                model_eq = input(f'Введите модель оргтехники ')
                price_eq = int(input(f'Введите цену за единицу товара '))
                quantity_eq = int(input(f'Введите количество поставляемой техники '))
                number_of_lists_eq = int(input(f'Введите заявленный объем работ (в листах) '))
                office_equipment = {'Производитель': brand_eq, 'Модель': model_eq, 'Цена за единицу товара': price_eq, 'Количество': quantity_eq, 
                                    'Заявленный объем работ (в листах)': number_of_lists_eq}
                self.list_office_equipment.append(office_equipment)
                print(f'Актуальный список оборудования - {self.list_office_equipment }')
            except:
                print(f'Ошибка ввода данных')

            print(f'Если вы хотите попробовать ввести еще, введите для продолжение соответственно -  Y/N')
            symbol = input()
            if symbol == 'N' or symbol == 'n':
                return f'Ввод завершен'
            
        
class Printer(OfficeEquipment):
    def print(self):
        return f'Заявленное от производителя количество напечатнных листов - {self.number_of_lists}'


class Scanner(OfficeEquipment):
    def scan(self):
        return f'Заявленное от производителя количество отсканированных листов - {self.number_of_lists}'


class Copier(OfficeEquipment):
    def copy(self):
        return f'Заявленный от производителя объем ксерокопий составляет - {self.number_of_lists} листов'



obj_p = Printer('Brother', 'HL-1202R', 40000, 20, 10000)
obj_s = Scanner('Canon', 'CanoScan LiDE 400', 5000, 5, 10000)
obj_c = Copier('HP', 'Ink Tank Wireless 415', 10000, 5, 15000)
print(obj_c)
print(obj_s)
print(obj_p)
print(obj_p.print())
print(obj_c.copy())
print(obj_s.scan())
print(obj_p.acceptance())







