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

product = []
while True:
    answer = input('Вы хотите внести новую позицию в базу? Наберите "да", для продолжения: ')
    if answer.lower() != "да":
        break
    name = input('Введите наименование товара: ')
    price = float(input('Введите цену товара: '))
    count = int(input('Введите количество товара: '))
    unit = input('Единиицы измерения: ')
    product.append((len(product), {'name': name, 'price': price, 'count': count, 'unit': unit}))

analytics = dict()
for _, item in product:
    for k, v in item.items():
        vl = analytics.get(k) or []
        if v not in vl:
            vl.append(v)
        analytics[k] = vl

print('Товар: ', product)
print('Аналитика: ', analytics)
