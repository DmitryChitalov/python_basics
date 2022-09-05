"""
4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо
выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень!
ВНИМАНИЕ: использование встроенной функции = задание не принято
Постараться придумать свой алгоритм без **
"""


def my_func(x, y):
    result = 1
    i = 1
    while i <= abs(y):
        result *= x
        i += 1
    return 1 / result


print(
    my_func(
        int(input("x: ")),
        int(input("y: "))
    )
)
