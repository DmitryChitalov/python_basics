products = []
i = 1
key_name = set()
key_price = set()
key_quantity = set()
key_unit = set()
product_dict = {}
print('Для ввыхода из режима ввода введите пустое название товара')
while True:
    print(F'"Заполните информацию о {i}-м товаре"')
    pr_name = input('Введите название товара: ')
    if pr_name != '':
        pr_price = input('Введите цену товара: ')
        pr_quantity = input('Введите количество товара: ')
        pr_unit = input('Введите единицу измерения товара: ')
        products.append((i, {'название': pr_name, 'цена': pr_price, 'количество': pr_quantity, 'ед': pr_unit}))
        key_name.add(pr_name)
        key_price.add(pr_price)
        key_quantity.add(pr_quantity)
        key_unit.add(pr_unit)
        i += 1
    else:
        break
print(f"Исходный список товаров: {products}\n")
product_dict = {'название': key_name, 'цена': key_price, 'количество': key_quantity, 'ед': key_unit}
for key, value in product_dict.items():
  print("{0}: {1}".format(key,value))







