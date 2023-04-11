"""
3. Реализовать функцию my_func(),
которая принимает три позиционных аргумента
и возвращает сумму наибольших двух аргументов.
"""


def my_func(arg1, arg2, arg3):
    """
    Функция возвращает сумму наибольших двух аргументов.
    """
    list_args = [arg1, arg2, arg3]
    max1 = max(list_args)
    list_args.remove(max1)
    max2 = max(list_args)
    return max1 + max2


print(f"{my_func(90, 170, 345)}")
