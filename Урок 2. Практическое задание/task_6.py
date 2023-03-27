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

i = 0
data_base = []

while True:
    name = input('Название товара: ')
    price = input('Цена: ')
    quantity = input('Количество: ')
    unit = input('Единица учета: ')
    i += 1
    data_base += [(i, {'название': name, 'цена': price, 'количество': quantity, 'ед': unit})]
    stop = input("Ввести следующий товар? y/n: ")
    if stop == "n":
        break

name = []
price = []
quantity = []
unit = []
resault = {}
for i in range(len(data_base)):
    name.append(data_base[i][1]["название"])
    price.append(data_base[i][1]["цена"])
    quantity.append(data_base[i][1]["количество"])
    unit.append(data_base[i][1]["ед"])

resault.update({"названия": name, "цены": price, "количество": quantity, "ед": unit})
print(resault)