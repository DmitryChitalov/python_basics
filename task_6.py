revenue = int(input("Укажите сумму выручки фирмы: "))
cost = int(input("Укажите размер издержек фирмы: "))
if revenue > cost:
    i = (revenue - cost) / revenue
    print(f"Рентабельность вашей фирмы равна {i}")
    number = int(input("Укажите число сотрудников вашей фирмы: "))
    i = i / number
    print(f"Прибыль фирмы в расчете на одного сотрудника равна {i}")
else:
    print("Ваша фирма нерентабельна")