"""
Задача 26: Напишите программу, которая на вход принимает
два числа A и B, и возводит число А в целую степень B с
помощью рекурсии.
A = 3 B = 5 -> 243 (3⁵)
A = 2 B = 3 -> 8
"""


def degree(var_a, var_b):
    if var_b == 0:
        return 1
    if var_b == -1:
        return 1 / var_a
    if var_b == 1:
        return var_a
    elif var_b > 1:
        return var_a * degree(var_a, var_b - 1)
    elif var_b < 0:
        return 1 / (var_a * 1 / (degree(var_a, var_b + 1)))


try:
    var_a, var_b = int(input("Введите число A: ")), int(
        input("Введите число B: "))
    print(f"Результат возведения в степень: {degree(var_a, var_b)}")
except ValueError:
    print("Работаем с числами")
