profit = int(input("Введите прибыль компании "))
costs = int(input("Введите издержки компании "))
number_stuff = int(input("Введите целое число количества сотрудников "))

revenue = profit - costs
profitability = int(profit / revenue)

if profit > costs:
    print("Профицит бюджета")
    print(f"рентабельность составила: {profitability}")
    revenue_stuff = int(revenue / number_stuff)
    print(f"Прибыль фирмы в расчете на {number_stuff} сотрудников составила: {revenue_stuff}")

elif profit < costs:
    print("Дефицит бюджета")
elif profit == costs:
    print("Фирма сработала в 0")