"""
4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо
выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень!
ВНИМАНИЕ: использование встроенной функции = задание не принято
Постараться придумать свой алгоритм без **
"""

def my_func(x, y):
    if y < 0:
        i = 1
        res = x
        while i < abs(x):
            res *= x
            i += 1
        print(f"Результат возведения х в степень y: {1 / res}")
    else:
        print("Число y - должно быть отрицательным")

print(my_func(2, -2))
