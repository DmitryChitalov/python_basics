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

input_revenue = input("Please, input revenue: ")
input_cost = input("Please, input cost: ")
if str.isdigit(input_revenue) & str.isdigit(input_cost):
    revenue = int(input_revenue)
    cost = int(input_cost)
    financial_result = revenue - cost
    if (financial_result > 0):
        efficiency = financial_result / revenue
        print(f"Your work is profitable, efficiency: {efficiency}")

        input_personal_count = input("Please, input personal count: ")
        if str.isdigit(input_personal_count):
            personal_count = int(input_personal_count)
            financial_result_for_person = financial_result / personal_count
            print(f"Revenue for one person: {financial_result_for_person}")
    else:
        print("Your work is unprofitable")
else:
    print("Error: revenue and cost is not a int value.")