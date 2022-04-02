revenue = int(input("Выручка: "))
costs = int(input("Издержки: "))
staff = int(input("Численность сотрудников: "))
profit = int(revenue - costs) // staff
if revenue > costs:
    print("Прибыль: ", profit)
else:
    print("Убыток: ", profit)
