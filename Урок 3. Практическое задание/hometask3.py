# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]

# Далее необходимо собрать аналитику о товарах. Реализовать словарь,
# в котором каждый ключ — характеристика товара, например название,
# а значение — список значений-характеристик, например список названий товаров.

# Пример:

# {
# “названия”: [“компьютер”, “принтер”, “сканер”],
# “цены”: [20000, 6000, 2000],
# “количества”: [5, 2, 7],
# “ед”: [“шт.”]
# }

products = []
for i in range(1, 4):
    print(f'Put down info about {i} product: ')
    product_name = input('name: ')
    product_price = int(input('price: '))
    product_count = int(input('count: '))
    product_measure = input('measure: ')
print(f'List of products: ')
product_names = []
product_prices = []
product_counts = []
product_measures = []
for i in products:
    product_names.append(i[1].get('name'))
    product_prices.append(i[1].get('price'))
    product_counts.append(i[1].get('count'))
    product_measures.append(i[1].get('measure'))
result = {
    'name': list(set(product_names)),
    'price': list(set(product_prices)),
    'count': list(set(product_counts)),
    'measure': list(set(product_measures))
}
print(f'Products report: \n{result}')

