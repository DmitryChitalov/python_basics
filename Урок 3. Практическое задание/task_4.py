"""
4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо
выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень!
ВНИМАНИЕ: использование встроенной функции = задание не принято
Постараться придумать свой алгоритм без **
"""

"""
4. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def my_fun1(var_a, var_b, var_c):
    if var_a >= var_c and var_b >= var_c:
        return var_a + var_b
    elif var_a >= var_b and var_c >= var_b:
        return var_a + var_c
    elif var_c >= var_a and var_b >= var_a:
        return var_b + var_c


print(my_fun1(1, 9, 6))


def my_fun2(var_a, var_b, var_c):
    list_1 = sorted([var_a, var_b, var_c])
    res = list_1[1] + list_1[2]
    print(res)


my_fun2(9, 1, 1)


my_fun2(int(input("Введите первое число: ")), int(
    input("Введите второе число: ")), int(input("Введите третье число: ")))
