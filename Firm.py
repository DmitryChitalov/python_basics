revenue = float(input("Введите выручку фирмы "))
costs = float(input("Введите издержки фирмы "))
if revenue > costs:
    print(f"Фирма работает с прибылью. Рентабельность выручки составила {revenue / costs:.2f}")
    employees = int(input("Введите количество сотрудников фирмы "))
    print(f"прибыль в расчете на одного сторудника сотавила {revenue / employees:.2f}")
elif revenue == costs:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")

