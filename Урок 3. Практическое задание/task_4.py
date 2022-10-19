"""
4. Программа принимает действительное положительное число x и целое
отрицательное число y. Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа
в степень!
ВНИМАНИЕ: использование встроенной функции = задание не принято
Постараться придумать свой алгоритм без **
"""


def my_pow(num, power):
    """
    возведение любого числа в степень

    :param num: число
    :param power: степень
    """
    if power == 0:
        return -1 if num < 0 else 1
    if num == 0:
        if power < 0:
            print(f"Division by zero 1/0^{power}")
            return None
        return 0

    result = pow_positive(num, abs(power))
    return result if power > 0 else 1 / result


def pow_positive(arg1, arg2):
    """возведение числа в положительную степень"""
    result = 1
    repeats = abs(arg2)
    while repeats > 0:
        result *= arg1
        repeats -= 1
    return result


print(f"0 ^ 0 = {my_pow(0, 0)}")
print(f"0 ^ 5 = {my_pow(0, 5)}")
print(f"-2 ^ 0 = {my_pow(-2, 0)}")
print(f"4 ^ 0 = {my_pow(4, 0)}")
print(f"-2 ^ 3 = {my_pow(-2, 3)}")
print(f"5 ^ -2 = {my_pow(5, -2)}")
print(f"2 ^ 4 = {my_pow(2, 4)}")
print(f"-3 ^ -2 = {my_pow(-3, -2)}")
print(f"0 ^ -5 = {my_pow(0, -5)}")
