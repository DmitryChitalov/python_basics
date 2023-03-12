products = []
for i in range(1, 4):
    print(f"Заполняем информацию по {i}-му товару")
    product_name = input("Название товара: ")
    product_price = int(input("Цена: "))
    product_count = int(input("Количество: "))
    product_measure =  input("Единица измерения: ")
    products.append((i, {'название': product_name, 'цена': product_price, 'количество':
                        product_count, 'eд': product_measure}))

print(f"Исходный список товаров: \n{products}")

product_names = []
product_prices = []
product_counts = []
product_measures = []
for i in products:
    product_names.append(i[1].get('название'))
    product_prices.append(i[1].get('цена'))
    product_counts.append(i[1].get('количество'))
    product_measures.append(i[1].get('eд'))

report = {'название': list(set(product_names)),
        'цена': list(set(product_prices)),
        'количество': list(set(product_counts)),
        'eд': list(set(product_measures))}

print(f"Отчет по списку товаров: \n{report}")
