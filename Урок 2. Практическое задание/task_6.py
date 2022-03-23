"""
6. *Реализовать структуру данных «Товары». Она должна представлять
собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у
пользователя.

Пример готовой структуры:
[
    (1, {“название”: “компьютер”, “цена”: 20000,
    “количество”: 5, “eд”: “шт.”}),
    (2, {“название”: “принтер”, “цена”: 6000,
    “количество”: 2, “eд”: “шт.”}),
    (3, {“название”: “сканер”, “цена”: 2000,
    “количество”: 7, “eд”: “шт.”})
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

inventory_list = []
i = 1
while True:
    inventory_list.append(
        (input('Enter product number '),
         dict({
             'name': str(input('Enter name ')),
             'price': float(input('Enter price ')),
             'amount': int(input('Enter amount ')),
             'units': str(input('Enter units '))})))

    if input('The product added. '
             'Do you want to add another product? y/n ') == 'n':
        break

    i += 1

print(f'product list: {inventory_list}')

output_dic = {}
for product in inventory_list:
    for key, value in product[-1].items():
        if key in output_dic:
            if value not in output_dic.get(key):
                output_dic.get(key).append(value)
        else:
            output_dic.update({key: [value]})

print(f'finale product list: {output_dic}')
