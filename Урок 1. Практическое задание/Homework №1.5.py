receipt = int(input("Введите значение выручки фирмы "))
cost = int(input("Введите значение издержек фирмы "))

if receipt > cost:
    profit = receipt - cost
    rent = profit / receipt
    print(f"Финансовый результат - прибыль. Ее величина - {profit}. "
          f"\nЗначит вычисляем рентабельность выручки (соотношение прибыли к выручке.)"
          f"\nРентабельность выручки = {rent}.")
    employee = int(input("Введите число сотрудников фирмы "))
    profit_employee = profit / employee
    print(f"Прибыль фирмы в расчете на одного сотрудника {profit_employee}.")
elif receipt == cost:
        print("Величина выручки равна издержкам фирмы.")
else:
    print("Убыток - издержки больше выручки.")
