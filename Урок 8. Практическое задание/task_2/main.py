"""
2. Задание на закрепление знаний по модулю json. Есть файл orders
в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий
его заполнение данными.

Для этого:
Создать функцию write_order_to_json(), в которую передается
5 параметров — товар (item), количество (quantity), цена (price),
покупатель (buyer), дата (date). Функция должна предусматривать запись
данных в виде словаря в файл orders.json. При записи данных указать
величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json()
с передачей в нее значений каждого параметра.

ПРОШУ ВАС НЕ УДАЛЯТЬ ИСХОДНЫЙ JSON-ФАЙЛ
ПРИМЕР ТОГО, ЧТО ДОЛЖНО ПОЛУЧИТЬСЯ

{
    "orders": []
}

вам нужно подгрузить JSON-объект
и достучаться до списка, который и нужно пополнять
а потом сохранять все в файл
"""

import json


def write_order_to_json(item, count, price, who, date):
    dict = {'item': '', 'quantity': '', 'price': '', 'buyer': '', 'date': ''}
    dict['item'] = item
    dict['quantity'] = count
    dict['price'] = price
    dict['buyer'] = who
    dict['date'] = date

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


dict = write_order_to_json(input('Товар: '), input('Количество: '),
                           input('Цена: '), input('Покупатель: '),
                           input('Дата: '))
check_order_to_json()
