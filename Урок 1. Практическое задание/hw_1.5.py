"""
5. Запросите у пользователя значения выручки и издержек фирмы.
 Определите, с каким финансовым результатом работает фирма.
Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки.
Выведите соответствующее сообщение.
"""
revenue_value = int(input("введите значение выручки: "))
value_of_costs = int(input("введите значение издержек: "))
if revenue_value > value_of_costs:
    print(f"Фирма работает с прибылью")
elif revenue_value < value_of_costs:
    print(f"Фирма работает с издержками")
else:
    print(f"Фирма работает без прибыли и без убытка")
