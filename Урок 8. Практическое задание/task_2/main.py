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
import os

def write_order_to_json(item, quantity, price, buyer, date):
    order = {
        "item": item,
        "quantity": quantity,
        "price": price,
        "buyer": buyer,
        "date": date
    }

    if os.path.exists('orders.json'):
        with open('orders.json', 'r') as f:
            data = json.load(f)
    else:
        data = {"orders": []}

    data['orders'].append(order)

    with open('orders.json', 'w') as f:
        json.dump(data, f, indent=4)

# Пример использования функции
write_order_to_json("Компьютер", 5, 23000, "Семенов", "2023-03-17")
write_order_to_json("Бумага", 3, 200, "Сидоров", "2023-03-18")
