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
cash = int(input("Введите значение выручки: "))
costs = int(input("Введите значение издержки: "))
if cash > costs:
    profit = cash - costs
    print("Ваша чистая прибыль: ", profit)
    workers = int(input("Сколько человек работает в вашей фирме? "))
    bonus = profit / workers
    print("Бонус для каждого сотрудника составит: ", bonus)
elif cash == costs:
    print("К сожалению, ваша прибыль равна убыткам")
else:
    loses = costs - cash
    print("Ваши убытки: ", loses)
