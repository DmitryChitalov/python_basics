print("Товары\nВведите информацию о товаре:")
i = 1
product = []
analytics = {}
list_name = []
list_price = []
list_amount = []
list_unit = []
while True:
    name = input("Введите название товара: ")
    price = input("Введите цену товара: ")
    amount = input("Введите количество товара: ")
    unit = input("Введите еденицу измерения: ")
    product_dict = {"название":name, "цена":price, "количество":amount, "ед":unit}
    product.append((i, product_dict))
    if name not in list_name:
        list_name.append(name)
    if price not in list_price:
        list_price.append(price)
    if amount not in list_amount:
        list_amount.append(amount)
    if unit not in list_unit:
        list_unit.append(unit)
    if int(input("Продолжить заполнять товары? (1 - Да, любое другое число - Нет): ")) != 1:
        break
    i += 1
analytics = {"название":list_name, "цена":list_price, "количество":list_amount, "ед":list_unit}
if int(input("Вывести список товаров? (1 - Да, любое другое число - Нет): ")) == 1:
    print(product)
if int(input("Вывести аналитику по товарам? (1 - Да, любое другое число - Нет): ")) == 1:
    print(analytics)



