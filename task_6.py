product_list = []
name_list = []
cost_list = []
number_list = []
a_list = []
i = 1
while i < 4:
    name = input("Введите название товара: ")
    cost = input("Введите цену товара: ")
    number = input("Введите количество товара: ")
    a = input("Введите единицу измерения товара: ")
    el = (i, {"название": name, "цена": cost, "количество": number,
                   "ед.": a})
    product_list.append(el)
    name_list.append(name)
    cost_list.append(cost)
    name_list.append(number)
    a_list.append(a)
    i = i + 1
print(product_list)
product_dict = {"название": name_list, "цена": cost_list,
                "количество": number_list, "ед.": a_list}
print(product_dict)