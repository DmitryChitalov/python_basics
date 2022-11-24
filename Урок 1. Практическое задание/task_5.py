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

def returnResault(result):
    if result > 0:
        return "Выручка больше издержек"
    elif result < 0:
        return "Издержки больше выручки"
    else:
        return f"Что-то идет не так, преятель. Ты работаешь в {result}"

profit_corp = 1500
costs_corp = 1500
result = profit_corp - costs_corp

profitability = costs_corp / profit_corp

employees = 10
profit_from_empl = profit_corp / employees * profitability

print(returnResault(result))
