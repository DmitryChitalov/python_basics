"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""
def my_func(*args):
    a = args[0]
    b = args[1]
    c = args[2]
    if a <= b and a <= c:
        return b * c
    elif b <= a and b <= c:
        return a * c
    else:
        return a * b

n_1 = int(input("Введите первое число: "))
n_2 = int(input("Введите второе число: "))
n_3 = int(input("Введите третье число: "))
print(my_func(n_1, n_2, n_3))

"""Второй вариант
def my_func(*args):
    list_n = sorted(args)
    return list_n[1] * list_n[2]
n_1 = int(input("Введите первое число: "))
n_2 = int(input("Введите второе число: "))
n_3 = int(input("Введите третье число: "))
print(my_func(n_1, n_2, n_3))"""
