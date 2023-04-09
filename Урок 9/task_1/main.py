"""
Задание 1.

Реализовать дескрипторы для любых двух классов.

"""

import json
import time
import string


# Как ещё можно реализовать повторный ввод ?

class CheckNumbers:
    def __set__(self, instance, value):
        if not type(value) is int:
            tru_value = ''
            while not type(tru_value) is int:
                try:
                    tru_value = int(
                        input(f"Ошибка ввода {value}, повторите: "))
                except ValueError:
                    pass
            instance.__dict__[self.attribute] = tru_value
        else:
            instance.__dict__[self.attribute] = value

    def __set_name__(self, owner, attribute):
        self.attribute = attribute


class CheckText:
    def __set__(self, instance, value):
        if not type(value) is str:
            tru_value = 0
            while not type(tru_value) is str:
                try:
                    tru_value = input(f"Ошибка ввода {value}, повторите: ")
                except ValueError:
                    pass
            instance.__dict__[self.attribute] = tru_value
        else:
            instance.__dict__[self.attribute] = value

    def __set_name__(self, owner, attribute):
        self.attribute = attribute


class CheckDate:
    def Datecheck(self, date):
        try:
            valid_date = time.strptime(date, '%m.%d.%Y')
            return date
        except ValueError:
            return 0

    def __set__(self, instance, date):
        value = self.Datecheck(date)
        if value == 0:
            valid_date = 0
            while valid_date == 0:
                try:
                    valid_date = self.Datecheck(
                        input(f"Ошибка ввода даты (ч.м.г), повторите: "))
                except ValueError:
                    pass
            instance.__dict__[self.attribute] = valid_date
        else:
            instance.__dict__[self.attribute] = value

    def __set_name__(self, owner, attribute):
        self.attribute = attribute


class OrderRecord:
    item = CheckText()
    count = CheckNumbers()
    price = CheckNumbers()
    who = CheckText()
    date = CheckDate()

    def __init__(self, item, count, price, who, date):
        self.item = item
        self.count = count
        self.price = price
        self.who = who
        self.date = date

    def write_order_to_json(self):
        dict = {'item': '', 'quantity': '', 'price': '', 'buyer': '',
                'date': ''}
        dict['item'] = self.item
        dict['quantity'] = self.count
        dict['price'] = self.price
        dict['buyer'] = self.who
        dict['date'] = self.date

        with open('home_orders.json', encoding='utf8-') as file:
            data = json.load(file)
            data["orders"].append(dict)
            with open('home_orders.json', 'w', encoding='utf-8') as outfile:
                json.dump(data, outfile, ensure_ascii=False, indent=4)


def check_order_to_json():
    with open('home_orders.json', encoding='utf8-') as file:
        data = json.load(file)
        list = data["orders"]
        [print(f"Ордер {list.index(el) + 1}: {el}") for el in list]


order = OrderRecord(input('Товар: '), int(input('Количество: ')),
                    int(input('Цена: ')),
                    input('Покупатель: '), input('Дата (ч.м.г): '))
order.write_order_to_json()
check_order_to_json()
