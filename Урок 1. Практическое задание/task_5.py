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
proceeds = int(input("Введите выручку фирмы: "))
costs = int(input("Введите издержки фирмы: "))
if proceeds < costs:
   print("Увы, ваша фирма работает в убыток ((")
elif proceeds == costs:
   print("К сожалению ваша фирма не приносит прибыли ((")
else:
   profit = proceeds - costs
   print(f"Поздравляю! Ваша фирма отработала с прибылью! Ее величина: {profit} ))")
   profitability = round(profit / proceeds, 1)
   print(f"Рентабельность выручки = {profitability}")
   staff = int(input("Введите численность сотрудников фирмы: "))
   profit_staff = round(profit / staff, 2)
   print(f"Прибыль фирмы в расчете на одного сотрудника = {profit_staff}")