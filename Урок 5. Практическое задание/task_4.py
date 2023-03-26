"""
Задание 4. Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75
Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтисть без создания массива!
"""


def sum_count(var_n, sum_n, temp):
    if var_n == 1:
        return sum_n
    elif var_n > 1:
        temp = temp / COUNT_DEL
        sum_n = sum_n + temp
        return sum_count(var_n - 1, sum_n, temp)


class NewEx(Exception):
    pass


COUNT_DEL = -2
try:
    var_n = int(input("Введите количество элементов: "))
    if var_n <= 0:
        raise NewEx()
    print(
        f"Сумма последовательности: {sum_count(var_n, 1, 1)} до {var_n} числа")
except ValueError:
    print('Работаем с натуральными числами')
except NewEx:
    print('Натуральные числа больше нуля')
