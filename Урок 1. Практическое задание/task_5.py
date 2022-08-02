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
income = int(input("Please enter income:"))
expenses = int(input("Please enter expenses:"))

if income - expenses > 0:
    profit = income - expenses
    profit_percent = profit / income * 100
    print(f"You have {profit_percent}% profit.")

    employees = int(input("Please enter the number of employees:"))
    profit_per_employee = profit / employees
    profit_per_employee_percent = profit_per_employee / profit * 100
    print(f"Profit per employee : {profit_per_employee}$ or {profit_per_employee_percent}%")

else:
    print("You have no profit, unfortunately")