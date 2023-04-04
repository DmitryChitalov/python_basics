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
goods_num = 0
goods_list = []
continue_question = ''
while continue_question != 'n':
    print(f"Введите информацию о товаре {goods_num + 1}:")
    goods_name = input("Название: ")
    goods_price = int(input("Цена: "))
    goods_qty = int(input("Количество: "))
    goods_measure = input("Ед.: ")
    goods_dict = {"Название": goods_name, "Цена": goods_price, "Количество": goods_qty, "Ед.": goods_measure}
    goods_tuple = (goods_num + 1, goods_dict)
    goods_list.append(goods_tuple)
    continue_question = (input("Продолжить ввод (введите 'n', чтобы закончить): "))
    goods_num += 1
goods_counter = 0
names_list = []
price_list = []
qty_list = []
measure_list = []
while goods_counter < goods_num:
    goods_tuple = goods_list[goods_counter]
    goods_dict = goods_tuple[1]
    names_list.append(goods_dict.get('Название'))
    price_list.append(goods_dict.get('Цена'))
    qty_list.append(goods_dict.get('Количество'))
    measure_list.append(goods_dict.get('Ед.'))
    goods_counter += 1
output_dict = {"Названия": names_list, "Цены": price_list, "Количества": qty_list, "Ед.": set(measure_list)}
for key, value in output_dict.items():
    print(key, ':', value)

