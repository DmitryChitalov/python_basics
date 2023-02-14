"""
Задание 5.

Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение. Если фирма отработала с прибылью,
вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите
прибыль фирмы в расчете на одного сотрудника.

Пример:
Введите выручку фирмы: 1000
Введите издержки фирмы: 500
Финансовый результат - прибыль. Ее величина: 500
Значит вычисляем рентабельность выручки (соотношение прибыли к выручке)
Рентабельность выручки = 0.5
Введите численность сотрудников фирмы: 10
Прибыль фирмы в расчете на одного сотрудника = 50.0
"""

revenue = float(input("Введите выручку фирмы: "))
costs = float(input("Введите издержки фирмы: "))
profit = revenue - costs

if profit > 0:
    print("Финансовый результат - прибыль. Ее величина:", profit)
    profitability = profit / revenue
    print("Рентабельность выручки =", profitability)
    num_employees = int(input("Введите численность сотрудников фирмы: "))
    profit_per_employee = profit / num_employees
    print("Прибыль фирмы в расчете на одного сотрудника =", profit_per_employee)
elif profit < 0:
    print("Финансовый результат - убыток. Его величина:", -profit)
else:
    print("Финансовый результат - ноль. Выручка равна издержкам.") 