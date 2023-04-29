"""
4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо
выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень!
ВНИМАНИЕ: использование встроенной функции = задание не принято
Постараться придумать свой алгоритм без **
"""


def my_func(x, y):
    denominator = abs(x)
    for i in range(abs(y)-1):
        denominator *= abs(x)

    result = 1 / denominator
    print(result)


while True:
    try:
        positive_num = float(input('Введите действительное положительное число: '))  # x
        negative_num = int(input('Введите целое отрицательное число: '))  # y
        if positive_num < 0 or negative_num > 0:
            raise ValueError
    except ValueError:
        print('Ошибка ввода данных. Попробуй еще раз.\n')
    else:
        my_func(positive_num, negative_num)
        break
