"""
4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо
выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень!
ВНИМАНИЕ: использование встроенной функции = задание не принято
Постараться придумать свой алгоритм без **
"""

def my_func(x, z):
    y = 1
    for i in range(abs(z)):
        y *= x
    if z >= 0:
        return y
    else:
        return 1 / y
x = int(input("Введите число x: "))
z = int(input("Введите число z: "))
print(my_func(x, z))







