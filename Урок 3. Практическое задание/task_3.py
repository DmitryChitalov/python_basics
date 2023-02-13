"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""

# 1 способ: спользуя функцию sort()
def my_func(var_1, var_2, var_3):
    my_val = [var_1, var_2, var_3]
    valsotr = sorted(my_val, reverse=False)
    return print(valsotr[1] + valsotr[2])


print(my_func(20, 10, 30))


# 2 способ:без функции sort()
def my_func2(var_1, var_2, var_3):
    return print(var_1 + var_2 + var_3 - min([var_1, var_2, var_3]))


print(my_func2(20, 10, 30))