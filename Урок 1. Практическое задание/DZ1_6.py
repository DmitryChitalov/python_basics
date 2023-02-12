revenue = int(input("Ваша прибыль: "))
cost = int(input("Ваши издержки "))
if revenue == cost:
    print("Ваша фирма работает в 0 ")
elif revenue > cost:
    print("Ваша фирма прибыльна")
    profit = revenue - cost
    rent = profit / revenue
    size = int(input("Введите количество сотрудников: "))
    profit_size = profit / size
    print("Ваша выручка ", profit, "Ваша рентабельность: ", rent, "Выручка на одного сотрудника ", profit_size)
else:
    print("Ваша фирма убыточна")

