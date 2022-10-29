"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def my_func_sort(var_1, var_2, var_3):
    my_tuple = (var_1, var_2, var_3)
    sorted_tuple = tuple(sorted(my_tuple))
    return sorted_tuple[-2] + sorted_tuple[-1]


def my_func(var_1, var_2, var_3):
    return var_1 + var_2 + var_3 - min(var_1, var_2, var_3)


print(my_func_sort(11, 3, 49))
print(my_func(11, 3, 49))
