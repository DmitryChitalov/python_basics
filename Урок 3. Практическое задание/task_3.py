"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def my_func(arg_1, arg_2, arg_3):
    args = []
    for i in (arg_1, arg_2, arg_3):
        args.append(i)
    args.sort(reverse=True)
    return_sort = args[0] + args[1]

    arg_max_1 = args.pop(args.index(max(args)))
    arg_max_2 = args.pop(args.index(max(args)))
    return_no_sort = arg_max_1 + arg_max_2

    return f"Результат используя функцию sort(): {return_sort}\nРезультат без функции sort(): {return_no_sort}"


print(my_func(7, 9, 5))
