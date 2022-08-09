revenue = input("Введите выручку фирмы в $: ")
costs = input("Введите издержки фирмы в $: ")
if int(revenue) - int(costs) > 0:
    print(f"Ваша фирма рентабильна, Вы зарабатываете {int(revenue) - int(costs)}$")
    employees = input("Введите количество сотрудников:")
    if employees.isdigit():
        print(f"В среднем каждый сотрудник зарабатывает: {(int(revenue) - int(costs)) / int(employees)}$")
    else:
        print("Ошибка ввода")
elif int(revenue) - int(costs) < 0:
    print("Ваша фирма работает в убыток")
else:
    print("Ваша фирма работает в 0")
