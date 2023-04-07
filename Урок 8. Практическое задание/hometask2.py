import json

def write_order_to_json(item, quantity, price, buyer, date):
    with open('orders.json') as f_n:
        dict_to_json = json.load(f_n)
        print(dict_to_json)
        dict_to_json['orders'].append({
            'item': item,
            'quantity': quantity,
            'price': price,
            'buyer': buyer,
            'date': date,
        })
    with open('orders.json', 'w') as f_w:
        json.dump(dict_to_json, f_w, indent=4)


if __name__ == "__main__":
    write_order_to_json('PC', 1, 3000, 'Petrov', '08.03.2020')
    write_order_to_json('PC_2', 2, 7000, 'Petrov', '08.03.2020')
    write_order_to_json('PS5', 3, 1500, 'Petrov', '08.03.2020')
    write_order_to_json('Scanner', 4, 900, 'Petrov', '08.03.2020')