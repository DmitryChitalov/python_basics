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

"""ФИО Суслин Александр"""

proceeds = int(input("Enter business proceeds: "))
costs = int(input("Enter business costs: "))

if 0 >= proceeds or 0 >= costs:
    print("Invalid proceeds or costs value.")
    exit()

if proceeds > costs:
    print("Successful business.")
    print(f"Profitability: {(proceeds - costs) / proceeds}")
    employees_number = int(input("How many employees? "))
    if 0 >= employees_number:
        print(f"Invalid employess number: {employees_number}")
        exit()

    print(f"Profit per employee: {(proceeds - costs) / employees_number}")

else:
    print("Unprofitable business.")
