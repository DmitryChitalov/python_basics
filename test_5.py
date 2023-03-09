plus = int(input("Введите выручку фирмы: "))
minus = int(input("Введите значение издержек: "))
clear_plus = plus - minus

if clear_plus > 0:
    print(f"Финансовый результат - прибыль. Ее величина {clear_plus}")

    print("Вычесляем рентабельность выручки(прибыль к выручке)")
    rent = clear_plus / plus
    print(f"Рентабельность выручки = {rent}")

    worker_num = int(input("Введите число сотрудников фирмы: "))
    worker_pr = clear_plus / worker_num
    print(f"Прибыль фиры в расчете на одного сотрудника = {worker_pr}")

elif clear_plus < 0:
    print(f"Финансивый результат - убыток. Ее величина {clear_plus}")

else:
    print("Выручка равна издержкам")
    



