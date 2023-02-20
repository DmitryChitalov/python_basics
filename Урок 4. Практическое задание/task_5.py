"""
5. Сделайте профилирование кода любого или любых выполненных заданий
с помощью модуля timeit, опишите результат
"""

from timeit import timeit

def my_func(x, y):
    """
    :param x: число, возводимое в степень
    :param y: степень
    :return: результат возведения x в y
    """
    result = x**y
    return result


print(timeit("my_func(4, -1)", globals=globals()))

def my_func2(x, y):
    while y < 0:
        den = x*x
        y += 1
        res = 1/den
    return res

print(timeit("my_func2(4, -1)", globals=globals()))

#Затраты времени на вычисление возведения числа в отрицательную степень меньше с использованием
#цикла, нежели встроенной арифметической функции. Результаты вычислений так же разные для обеих функций