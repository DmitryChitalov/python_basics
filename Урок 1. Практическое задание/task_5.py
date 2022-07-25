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

revenue = int(input("Введите выручку фирмы: "))
costs = int(input("Введите издержки фирмы: "))
profit = revenue - costs
ros = costs / revenue
if revenue > costs:
    print(f"Финансовый результат: Прибыль. Ее величина: {profit}")
elif revenue == costs:
    print("Финансовый результат: Работа в ноль")
else:
    print("Финансовый результат: Убыток")
print(f"Рентабельность выручки = {ros}")
employees = int(input("Введите численность сотрудников фирмы: "))
print("Прибыль фирмы в расчете на одного сотрудника = ", profit / employees)
