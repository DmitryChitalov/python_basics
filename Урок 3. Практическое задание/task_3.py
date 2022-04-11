"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


# без sort
def my_func(arg_1, arg_2, arg_3):
    """ Возвращает сумму больших аргументов
    arg_1 - int
    arg_2 - int
    arg_3 - int
    return - int
    """
    a = max(arg_1, arg_2, arg_3) + max(min(arg_1, arg_2), min(arg_1, arg_3), min(arg_2, arg_3))
    return a


print(my_func(3, 2, 3))


# через sort
def my_func_2(arg_1, arg_2, arg_3):
    """ Возвращает сумму больших аргументов
    arg_1 - int
    arg_2 - int
    arg_3 - int
    return - int
    """
    new_list = [arg_1, arg_2, arg_3]
    new_list.sort()
    return new_list[1] + new_list[2]


print(my_func_2(7, 100, 8))
