"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def my_func(a, b, c):
    """функцию my_func(), которая принимает три позиционных аргумент"""
    list_args = [a, b, c]
    list_args.sort()
    return list_args[2] + list_args[1]


def my_func_no_sort(a, b, c):
    """функцию my_func(), которая принимает три позиционных аргумент без функции sort()"""
    list_args = [a, b, c]
    list_args.remove(min(list_args))
    return sum(list_args)


print(my_func(7, 1, 10))
print(my_func_no_sort(7, 4, 10))
