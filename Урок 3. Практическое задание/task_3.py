"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def my_func(var_1, var_2, var_3):
    sum_var = [int(var_1), int(var_2), int(var_3)]
    sum_var.sort()
    sum_var.reverse()
    return sum_var[0] + sum_var[1]


print(my_func(10, 2, 9))


def my_func2(var_1, var_2, var_3):
    sum_var = [int(var_1), int(var_2), int(var_3)]
    prom = max(sum_var)
    sum_var.pop(sum_var.index(max(sum_var)))
    result = max(sum_var) + prom
    return result


print(my_func2(10, 2, 9))

