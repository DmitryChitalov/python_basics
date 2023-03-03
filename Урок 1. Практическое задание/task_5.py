#ветвления
revenue = int(input("Введите выручку фирмы: "))
costs = int(input("Введите издержки фирмы: "))
if revenue > costs:
    number_of_employees= int(input("Введите количество сотрудников фирмы: "))
    print(f" Рентабельность выручки: {((revenue - costs) / revenue):.3f}, рублей!")
    print(f" Фирма работает с прибылью в расчете на 1 сотрудника: {(revenue - costs)/number_of_employees}, рублей!")

elif revenue == costs:
    print(f" Фирма на гране. Прибыль - {revenue - costs}, рублей!")
else:print(f" Фирма работает с убытком: {revenue - costs}, рублей!")
