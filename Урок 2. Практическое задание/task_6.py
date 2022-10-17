"""
6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

Пример готовой структуры:
[
    (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
    (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
    (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]

Далее необходимо собрать аналитику о товарах. Реализовать словарь,
в котором каждый ключ — характеристика товара, например название,
а значение — список значений-характеристик, например список названий товаров.

Пример:

{
“названия”: [“компьютер”, “принтер”, “сканер”],
“цены”: [20000, 6000, 2000],
“количества”: [5, 2, 7],
“ед”: [“шт.”]
}
"""

product_list = []

product_number = 1
while True:
    product_name = input("Название продукта: ")
    product_price = int(input("Цена: "))
    product_count = int(input("Количество: "))
    product_unit = input("Единица измерения: ")

    product_params = {"название": product_name, "цена": product_price,
                      "количество": product_count, "eд": product_unit}
    product_list.append((product_number, product_params))
    product_number += 1

    add_next = True
    while True:
        can_add = input("Добавить еще один продукт (Y/N)? ")
        if can_add == "Y":
            break
        if can_add == 'N':
            add_next = False
            break
        print("Введено некоректное значение!")

    if not add_next:
        break

params_products = []
for product in product_list:
    params_by_product = []
    for key, val in product[1].items():
        params_by_product.append(val)
    params_products.append(tuple(params_by_product))

product_properties = list(zip(*params_products))

product_analytics = {"названия": None, "цены": None, "количества": None,
                     "ед": None}
product_index = 0
for key in product_analytics.items():
    product_analytics[key] = set(product_properties[product_index])
    product_index += 1

print(product_analytics)
