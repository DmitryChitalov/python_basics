"""
4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо
выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень!
ВНИМАНИЕ: использование встроенной функции = задание не принято
Постараться придумать свой алгоритм без **
"""
def my_func(a, b):
    var = 1
    for i in range(b*(-1)):
        var *= a
    return 1 / var


x = int(input('Input first number: '))
y = int(input('Input second number: '))
print(my_func(x, y))