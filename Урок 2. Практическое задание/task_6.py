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
goods_counter = 0
g_list = []
while True:
    good_name = input('Введите название товара : ')
    good_cost = float(input('Введите цену товара: '))
    good_amount = int(input('Введите количество товара: '))
    good_unit = input(
        'Единица измерения количества товара(шт., уп. и т.п. ): ')
    nonstop = ''
    goods_counter = goods_counter + 1
    my_dict = dict(название=good_name, цена=good_cost,
                   количество=good_amount, ед=good_unit)
    my_gtuple = (goods_counter, my_dict)
    g_list.append(my_gtuple)
    # print(g_list)
    nonstop = input('Желаете продолжить ввод товаров?: Yes/No (Y/n) \n')
    if nonstop == 'n' or nonstop == 'No' or nonstop == 'no' or nonstop == 'N':
        break
    else:
        pass
anal_dict = {}
names_list, costs_list, amnts_list, units_list = [], [], [], []
for el in g_list:
    for i in el:
        if type(i) is dict:
            names_el = i.get('название')
            names_list.append(names_el)
            costs_el = i.get('цена')
            costs_list.append(costs_el)
            amnts_el = i.get('количество')
            amnts_list.append(amnts_el)
            units_el = i.get('ед')
            units_list.append(units_el)
# на случай, если нужны только уникальные значения единиц измерения
units_set = set(units_list)
units_list = list(units_set)
anal_dict = {"названия": names_list, "цены": costs_list,
    "количества": amnts_list, "единицы": units_list}
print(anal_dict)
