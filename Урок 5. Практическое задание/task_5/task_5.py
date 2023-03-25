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
Решит
"""


def func1(many):
    right_fun = int(many * (many + 1) / 2)
    left_fun = 0

    def proof_func(bub):
        nonlocal left_fun, right_fun
        if bub < 1:
            return print(f'{left_fun} = {right_fun}')
        else:
            left_fun += bub
            proof_func(bub - 1)

    proof_func(many)


many = int(input('Введите границу множества : '))
func1(many)
