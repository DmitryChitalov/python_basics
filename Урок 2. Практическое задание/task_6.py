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
params = {}
n = int(input("Введите количество товаров: "))
product_number = 1
for ind in range(n):
    name = input("Введите наименование: ")
    price = int(input("Введите цену: "))
    count = int(input("Введите количество: "))
    ed = input("Введите единицу измерения: ")
    params = {'name': name, 'price': price, 'amount': count, 'unit': ed}
    product_list.append((product_number, params))
    product_number += 1
print("Итоговая структура: ", product_list)
name_dik = {}
name_dik_help = []
price_dik = {}
price_dik_help = []
count_dik = {}
count_dik_help = []
ed_dik = {}
ed_dik_help = []
for imd in range(n):
    name_dik_help.append(product_list[imd][1]['name'])
    price_dik_help.append(product_list[imd][1]['price'])
    count_dik_help.append(product_list[imd][1]['amount'])
    ed_dik_help.append(product_list[imd][1]['unit'])
    name_dik = {'name': name_dik_help}
    price_dik = {'price': price_dik_help}
    count_dik = {'amount': count_dik_help}
    ed_dik = {'unit': ed_dik_help}
print(name_dik)
print(price_dik)
print(count_dik)
print(ed_dik)
