revenue = int(input("Введите выручку фирмы "))
costs = int(input("Введите издержки фирмы "))
profit = revenue - costs
if profit > 0:
    print(f"Фирма отработала с прибылью: {profit}")
    profit_b = profit / revenue
    print("Рентабельность", profit_b)
    manager = int(input(f"Укажите численность сотрудников:"))
    profit_man = profit / manager
    print(f"Прибыль на одного сотрудника составила: {profit_man}")
elif profit < 0:
    print("Фирма работает в убыток")
else:
    print("Фирма ничего не заработала ")











