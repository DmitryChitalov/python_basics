"""
6. Если фирма отработала с прибылью, вычислите рентабельность выручки.
Это отношение прибыли к выручке.
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.
"""
revenue_value = int(input("введите значение выручки: "))
value_of_costs = int(input("введите значение издержек: "))
if revenue_value > value_of_costs:
    print(f"Фирма работает с прибылью")
    profitability_of_revenue = (revenue_value - value_of_costs) / revenue_value
    print(f"рентабельность выручки равна : {profitability_of_revenue}")
    number_employees_company = int(input("введите численность сотрудников фирмы: "))
    print(
        f"прибыль фирмы в расчёте на одного сотрудника ={(revenue_value - value_of_costs) / number_employees_company}")
elif revenue_value < value_of_costs:
    print(f"Фирма работает с издержками")
else:
    print(f"Фирма работает без прибыли и без убытка")
