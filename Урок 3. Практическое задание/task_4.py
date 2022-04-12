"""
4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо
выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень!
ВНИМАНИЕ: использование встроенной функции = задание не принято
Постараться придумать свой алгоритм без **
"""

def my_func(integer, degree):
    result = 1
    count = 0
    if 0 == degree:
        return result;
    if 0 == integer:
        return 0
    if 0 > degree:
        while count > degree:
            result = result / integer
            count -= 1
        return result
    else:
        while count < degree:
            result = result * integer
            count += 1
        return result

print(f"{my_func(8, -4)}")
