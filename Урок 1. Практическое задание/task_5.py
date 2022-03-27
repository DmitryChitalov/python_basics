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

vir = int(input("Я даже могу посчитать рентабельность вашей фирмы, введите размер выручки вашей компании: "))
izd = int(input("Теперь издержки (затраты) вашей фирмы:"))
fin = vir - izd
rent = fin / vir * 100
if fin > 0:
    print(f"Поздравляю, ваша фирма прибыльна! Прибыль составляет: {fin}. Рентабельность составляет: {'%.2f' % rent} %")
    sot = int(input("Укажите пожалуйста численность сотрудников в вашей организации?"))
    sot_rent = fin / sot
    print(f"Прибыль фирмы в расчете на одного сотрудника составляет:{'%.2f' % sot_rent} ")
elif fin == 0:
    print("Ваша фирма работает в '0', поднажмите)")
elif fin <= -1:
    print(f"К сожалению ваша фирма работает в убыток.. Убыток на данный момент: {fin}")
else:
    print("Ошибка.")
