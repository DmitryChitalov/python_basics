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
goods = []
goods_analyse = {
    'название': [],
    'цена': [],
    'количество': [],
    'ед': []
}
count = 1
while True:
    name = input('Введите название товара: ')
    price = int(input('Введите цену товара: '))
    quantity = int(input('Введите количество товара: '))
    measure = input('Введите единицу измерения товара: ')
    goods.append((count, {'название': name, 'цена': price, 'количество': quantity, 'ед': measure}))
    count = count + 1
    print('Товары')
    for good in goods:
        print(good)
        for item in good[1].items():
            if item[1] not in list(goods_analyse.items())[list(good[1].items()).index(item)][1]:
                list(goods_analyse.items())[list(good[1].items()).index(item)][1].append(item[1])
    print('Аналитика о товарах')
    for item in goods_analyse.items():
        print(item)
