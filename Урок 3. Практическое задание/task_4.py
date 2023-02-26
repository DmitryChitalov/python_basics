"""
4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо
выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень!
ВНИМАНИЕ: использование встроенной функции = задание не принято
Постараться придумать свой алгоритм без **
"""

# def my_func_1(x, y):
#     return x ** y
def my_func_2(x, y):
    counter = 1
    result = 1 / x
    while counter < abs(y):
        result = result * (1 / x)
        counter += 1
    return result
#
# print(f'Возведения степени вариантом 1: '
#       f'{my_func_1(int(input('Основание степени Х: ')), int(input('Показатель степени Y: ')))}')
#
print(f'Возведения степени вариантом 2: '
      f'{my_func_2(int(input('Основание степени Х: ')), int(input('Показатель степени Y: ')))}')