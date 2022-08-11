my_list = []
i = 1
my_dict = {"name": [], "price": [], "amount": []}
while True:
    name = input("Input name of product: ")
    price = float(input("Pls input the price: "))
    amount = int(input("input amount of product: "))
    t = (i, {"name": name, "price": price, "amount": amount})
    my_list.append(t)
    my_dict["name"].append(name)
    my_dict["price"].append(price)
    my_dict["amount"].append(amount)

    t_1 = input("Add another one product? - Y ")
    if t_1 == "Y":
        i = i + 1
        continue
    else:
        print('Have a good day!')
        break
print(my_list)
