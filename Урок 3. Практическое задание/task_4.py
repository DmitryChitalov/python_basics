"""
4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо
выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень!
ВНИМАНИЕ: использование встроенной функции = задание не принято
Постараться придумать свой алгоритм без **
"""

def my_fun(x, y):
    s = x
    for i in range(0, abs(y) - 1 if y > 0 else abs(y)):
        s *= x 
    return x / s if y < 0 else s

print(my_fun(int(input("Введите x = ")), int(input("Введите y = "))))
