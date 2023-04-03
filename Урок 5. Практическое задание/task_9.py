"""
Задача 28: Напишите рекурсивную функцию sum(a, b),
возвращающую сумму двух целых неотрицательных чисел. Из
всех арифметических операций допускаются только + 1 и - 1.
Также нельзя использовать циклы.
2 2
4
"""


def total(var_a, var_b):
    if var_a == 1 and var_b == 1 or var_a == 0 or var_b == 0:
        return var_a + var_b
    elif var_a == var_b:
        return total(var_a - 1, var_b) + 1
    elif var_a > var_b:
        return total(var_a - 1, var_b) + 1
    elif var_a < var_b:
        return total(var_a, var_b - 1) + 1


class NewEx(Exception):
    pass


try:
    var_a, var_b = int(input("Введите число A: ")), int(
        input("Введите число B: "))
    if var_a < 0 or var_b < 0:
        raise NewEx()
    print(f"Сумма чисел полученная рекурсивным методом: {total(var_a, var_b)}")
except ValueError:
    print("Работаем с числами")
except NewEx:
    print("Работаем c неотрицательными числами")
