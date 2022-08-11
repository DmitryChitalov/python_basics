"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def my_func(arg1, arg2, arg3):
    """ My func description """
    # Способ1
    all_arg = [arg1, arg2, arg3]
    all_arg.sort()
    sum_two_max_args_1 = all_arg[1] + all_arg[2]
    # Способ2
    all_arg.remove(min(arg1, arg2, arg3))
    sum_two_max_args_2 = all_arg[0] + all_arg[1]
    return sum_two_max_args_1, sum_two_max_args_2


print(my_func((int(input("Введите первое число: "))),
              (int(input("Введите второе число: "))),
              (int(input("Введите третье число: ")))))
