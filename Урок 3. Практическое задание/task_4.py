"""
4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо
выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень!
ВНИМАНИЕ: использование встроенной функции = задание не принято
Постараться придумать свой алгоритм без **
"""


def my_func(x, y):
    result_local = x
    for z in range(y * (-1) + 1):
        result_local /= x
    return result_local


def first_positive_arg():
    number = -1
    while number < 0:
        try:
            number = float(input("Ввдеите действительное положительное число: "))
        except ValueError:
            print("Я сказал действительное число!")
            number = -1
    return number


def second_negative_arg():
    number = 1
    while number >= 0:
        try:
            number = int(input("Ввдеите целое отрицательное число: "))
        except ValueError:
            print("Я сказал целое ОТРИЦАТЕЛЬНОЕ число!")
            number = 1
    return number


a = first_positive_arg()
b = second_negative_arg()

result = my_func(a, b)

print("Результат: ", result)
