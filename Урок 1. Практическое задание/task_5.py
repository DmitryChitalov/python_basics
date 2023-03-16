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

revenue = int(input("Input revenue:"))
cogs = int(input("Input COGS:"))  # COGS = cost of goods sold

prof = False  # признак прибыльности компании

if revenue != cogs:
    if revenue > cogs:
        print(f"The company is profitable. Profit = {revenue - cogs}")
        prof = True
    elif revenue < cogs:
        print("The company is unprofitable")
elif revenue == cogs:
    print("The company operates at break-even point")

if prof:
    profit = revenue - cogs
    ror = profit / revenue
    print("Return on revenue ratio: %.3f" % ror)
    employees_num = int(input("Input number of employees:"))
    print("Profit per employee: %.3f" % (profit / employees_num))
