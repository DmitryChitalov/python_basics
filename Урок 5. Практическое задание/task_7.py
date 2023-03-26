"""
Задание 7. Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.
Пример:
для n = 5
1+2+3+4+5 = 5(5+1)/2
Нужно написать рекурсивную ф-цию только для левой части выражения!
Результат нужно сверить с правой частью.
Правой части выражения в рекурсивной ф-ции быть не должно!
Решите через рекурсию. В задании нельзя применять циклы.
"""


def progression(var_n, res_left):
    if var_n == 1:
        return res_left
    elif var_n > 1:
        res_left = res_left + var_n
        return progression(var_n - 1, res_left)


class NewEx(Exception):
    pass


try:
    var_n = int(input("Введите количество элементов: "))
    if var_n <= 0:
        raise NewEx()
    res_right = int(var_n * (var_n + 1) / 2)
    print(f"Равенство выполняется {progression(var_n, 1)} = {res_right}")
except ValueError:
    print("Работаем с натуральными числами")
except NewEx:
    print("Натуральные числа больше нуля")
