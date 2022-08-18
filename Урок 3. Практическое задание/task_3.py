"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""
### Первый способ (sort)
print("Первый способ...")


def my_sum():
    try:
        a1 = float(input("Введите первое число: "))
        a2 = float(input("Введите второе число: "))
        a3 = float(input("Введите третье число: "))
    except ValueError:
        print("Нужно вводить числа")
        return
    my_list = [a1, a2, a3]
    my_list.sort()
    s = my_list[1] + my_list[2]
    return s


print(my_sum())

### Второй способ
print("Второй способ...")


def my_sum2():
    try:
        a1 = float(input("Введите первое число: "))
        a2 = float(input("Введите второе число: "))
        a3 = float(input("Введите третье число: "))
    except ValueError:
        print
        "Нужно вводить числа"
        return
    if a1 > a2:
        if a2 > a3:
            s = a1 + a2
        else:
            s = a1 + a3
    elif a3 > a1:
        s = a2 + a3
    else:
        s = a2 + a1
    return s


print(my_sum2())
