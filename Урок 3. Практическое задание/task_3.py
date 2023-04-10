"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def my_func_sort(arg1, arg2, arg3):
    list_number = sorted([arg1, arg2, arg3])
    return sum(list_number[1:])


def my_func(arg1, arg2, arg3):
    return arg1 + arg2 + arg3 - min(arg1, arg2, arg3)


print(my_func_sort(3, 2, 4))
print(my_func(3, 2, 4))
