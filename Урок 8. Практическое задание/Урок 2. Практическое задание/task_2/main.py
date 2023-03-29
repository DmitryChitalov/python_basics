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


def write_order_to_json(item, quantity, price, buyer, date):
    with open('orders.json') as a:
        dict_to_json = json.load(a)
        print(dict_to_json)
        dict_to_json['orders'].append({
            'item': item,
            'quantity': quantity,
            'price': price,
            'buyer': buyer,
            'date': date,
        })
    with open('orders.json', 'w') as b:
        json.dump(dict_to_json, b, indent=4)


if __name__ == "__main__":
    write_order_to_json('fish', 53, 100, 'Ivanov', '01.01.2021')
    write_order_to_json('meat', 12, 500, 'Ivanov', '05.03.2018')
    write_order_to_json('chicken', 1, 100, 'Ivanov', '08.03.2022')
    write_order_to_json('milk', 6, 200, 'Ivanov', '01.01.2023')
