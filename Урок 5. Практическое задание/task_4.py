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

n = int(input("Введите натуральное число: "))


def sum_pro(num):
    if num == 1:
        return 1
    return -0.5 ** num + sum_pro(num - 1)


print(f"Количество элементов - {n}, их сумма - {sum_pro(n - 1)}")