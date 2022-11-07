money = int(input("Введите вырочку фирмы"))
costs = int(input("Введите издержки фирмы"))
res = money - costs
rent = costs / money
people = int(input("Введите количество сотрудников"))
money_one = res / people

print(f"Финансовый результат {res}, рентабельность - {rent}, деньги одного сотрудника {money_one}.")
