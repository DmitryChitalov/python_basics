"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""
#Task_3
def func_sort(var_1, var_2, var_3):
    my_tuple = (var_1, var_2, var_3)
    sorted_tuple = tuple(sorted(my_tuple))
    return sorted_tuple[-2] + sorted_tuple[-1]
