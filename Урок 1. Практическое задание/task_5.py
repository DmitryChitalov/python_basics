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
potok_plus = int(input("введите выручку фирмы"))
potok_minus = int(input("введите издержки фирмы"))
if potok_plus > potok_minus:
    pr = potok_plus - potok_minus
    print(f" ваш финансовый результат - прибыль. Ее величина {pr}")
    rent = pr / potok_plus
    print(f" Рентабельность вашей выручки {rent}")
    pers = int(input("Введите количество сотрудников "))
    pr_pers=pr / pers
    print(f" Прибыль в расчете на 1 сотрудника {pr_pers}")
elif potok_plus < potok_minus:
    print(f" ваш финансовый результат - убыток")
elif potok_plus == potok_minus:
    print(f" ваш финансовый результат - 0")
