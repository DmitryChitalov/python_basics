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

incoming = int(input("Введите выручку фирмы "))
charges = int(input("Введите издержки фирмы "))
profit = incoming - charges
print(f"Величина прибыли: {profit}")
if profit > 0:
    profitability = profit / incoming
    print(f"Рентабельность выручки = {profitability}")
    employees = int(input('Введите численность сотрудников '))
    employee_profit = profit / employees
    print(f"Прибыль фирмы в расчете на одного сотрудника = {employee_profit}")
else:
    print("Ой, похоже вы работаете не ради прибыли")
