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
spiski = []
tovar = {'название': '', 'описанине': '', 'цена.за 1 ед': '', 'количество': '', 'ед.измер': ''}
analytics = {'название': [], 'описанине': [], 'цена.за 1 ед': [], 'количество': [], 'ед.измер': []}
num = 0
control = None
line = "-" * 30

while True:
    control = input("Для выхода нажмите '1', для продолжения нажмите '2', для аналитики нажмите '3': ")
    if control == '1':
        break
    elif control == '3':
        if len(spisok) == 0:
            print("Пустая строка")
            continue
        print(f'\tТекущая аналитика\n{line}')
        for key, value in analytics.items():
            value = list(set(value))
            print(f'{key[:25]:>10}: {value}\n{line}')
    elif control == '2':
        num += 1
        spisok = dict(tovar)
        for f in tovar.keys():
            pozic = input(f'Введите позицию "{f}": ')
            spisok[f] = pozic if (f == 'название' or f == 'описанине' or f == 'ед.измер') else pozic
            analytics[f].append(pozic)
        spiski.append((num, spisok))
    else:
        print("Неправильный ввод")

