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
#Выполнение шестого задания
goods = []
template = {'название': '', 'цена': '', 'количество': '', 'ед': ''}
analytics = {'название': [], 'цена': [], 'количество': [], 'ед': []}
num = 0
control = None
line = "-" * 30

while True:
    control = input("Для выхода нажмите 'В', для продолжения нажмите 'П', для аналитики нажмите 'А': ").upper()
    if control == 'В':
        break
    elif control == 'А':
        if len(goods) == 0:
            print("Нет элементов для аналитики")
            continue
        print(f'\tТекущая аналитика\n{line}')
        for key, value in analytics.items():
            value = list(set(value))
            print(f'{key[:25]:>10}: {value}\n{line}')
    elif control == 'П':
        num += 1
        good = dict(template)
        for f in template.keys():
            feature = input(f'Введите характеристику "{f}": ')
            good[f] = feature if (f == 'название' or f == 'ед') else int(feature)
            analytics[f].append(feature)
        goods.append((num, good))
    else:
        print("Неправильный ввод")