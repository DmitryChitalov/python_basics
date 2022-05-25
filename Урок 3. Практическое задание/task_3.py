"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def my_func(arg_1, arg_2, arg_3):
    my_list = (arg_1, arg_2, arg_3)
    new_list = sorted(my_list)
    return new_list[1] + new_list[2]


print(my_func(1, 10, 3))


def my_func_2(arg_1, arg_2, arg_3):
    return arg_1 + arg_2 + arg_3 - (min(arg_1, arg_2, arg_3))


print(my_func_2(100, 30, 40))


def my_func_3(arg_1, arg_2, arg_3):
    my_list = [arg_1, arg_2, arg_3]
    my_list.remove(min(arg_1, arg_2, arg_3))
    return sum(my_list)


print(my_func_3(120, 10, 9))
