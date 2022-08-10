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

# Выводим название программы
print(f'Программа реализации структуры даных "Товары"')

# Заполняем Структуру данных
product_list = []
temp_answer = 'да'
temp_index = 1
temp_list = []

while temp_answer == 'да' or temp_answer == 'y':
    temp_list = input(f'Введите характеристики товара в формате: \n'
                      'Название Цена Количество Ед.изм\n').split()
    temp_dict = {'Название': temp_list[0], 'Цена': temp_list[1], 'Количество': temp_list[2],
                 'Ед.изм': temp_list[3]}
    product = (temp_index, temp_dict)
    product_list.append(product)
    temp_index += 1
    temp_answer = input('Продолжить ввод (да/нет) ')

# Объявляем переменные для выборки
temp_names = []
temp_cost = []
temp_counts = []
temp_units = []

# Формируем выборку словарь
for temp_index in range(0, len(product_list)):
    temp_names.append(product_list[temp_index][1]['Название'])
temp_names = list(set(temp_names))

for temp_index in range(0, len(product_list)):
    temp_cost.append(product_list[temp_index][1]['Цена'])
temp_cost = list(set(temp_cost))

for temp_index in range(0, len(product_list)):
    temp_counts.append(product_list[temp_index][1]['Количество'])
temp_counts = list(set(temp_counts))

for temp_index in range(0, len(product_list)):
    temp_units.append(product_list[temp_index][1]['Ед.изм'])
temp_units = list(set(temp_units))

total_dict = {'Название': temp_names, 'Цена': temp_cost, 'Количество': temp_counts, 'Ед.изм': temp_units}

# Выводим на экран построчно
for temp_index in ['Название', 'Цена', 'Количество', 'Ед.изм']:
    print(f'{temp_index}: {total_dict.get(temp_index)}')
