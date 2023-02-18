"""
4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо
выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень!
ВНИМАНИЕ: использование встроенной функции = задание не принято
Постараться придумать свой алгоритм без **
"""


def my_func(x, y):
    """
    Takes a real positive number x and a negative integer y
    :param int|float x: positive number
    :param int y: negative integer
    :return: x ** -y
    """
    res = None
    if isinstance(y, int) and x > 0:
        if y < -1:
            n = 1
            while n < -y:
                n += 1
                res = x * x if res is None else res * x
            res = 1 / res
        elif y == -1:
            res = 1 / x
    return res


print(my_func(33, -1))
