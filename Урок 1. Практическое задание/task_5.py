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

"""Код определяет, с каким финансовым результатом работает фирма."""
profit = int(input('Введите прибыль: '))                 #Запрашиваем данные у пользователя
loss = int(input('Введите убыток: '))
if profit >= loss:                                      #Если прибль превышает убыток
    delta = profit - loss
    print("Прибыль составляет: ", delta)                 #Вывод результата прибыли
elif profit <= loss:                                    #Если убыток превышает прибль
    delta = loss -profit
    print("Убыток составляет: ", delta)                 #Вывод результата убытка
