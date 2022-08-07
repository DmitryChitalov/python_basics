"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def my_func(arg1, arg2, arg3):
    args_set = []
    for i in (arg1, arg2, arg3):
        args_set.append(i)
    args_set.sort(reverse=True)
    return_sorted = args_set[0] + args_set[1]

    arg_max1 = args_set.pop(args_set.index(max(args_set)))
    arg_max2 = args_set.pop(args_set.index(max(args_set)))
    return_no_sort = arg_max1 + arg_max2

    return f"+ sort(): {return_sorted}\n- sort(): {return_no_sort}"


print(my_func(5, 1, 2))
# + sort(): 7
# - sort(): 7
