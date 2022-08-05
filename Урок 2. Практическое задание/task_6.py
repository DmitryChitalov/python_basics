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
stats_goods = {}

for i in range(1,4):                                                  # Ask for user input 3 times
    category_number = i
    category = input("Please enter category name:")
    price = int(input("Please enter the price:"))
    stock = int(input("Please enter the amount in stock:"))
    pieces = input("Please enter the pieces:")

    goods_dictionary = {
        "Category" : category,
        "Price" : price,
        "Stock" : stock,
        "Pieces" : pieces
    }

    goods_tuple = (category_number, goods_dictionary)
    goods.append(goods_tuple)
    print(goods)
    
# Create new empty dictionary, with categories names
for i in goods:
    information=i[1]
    for key,value in information.items():
        stats_goods[key] = []

# Get the stats
for cat in goods:
    information = cat[1]
    for key,value in information.items():
        stats_goods[key].append(value)

for i in stats_goods:
    if i == "Pieces":
        print(i,set(stats_goods[i]))
    else:       
        print(i,stats_goods[i])