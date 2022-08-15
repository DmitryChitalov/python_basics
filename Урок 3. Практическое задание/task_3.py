"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def my_fun_with_sort(arg1, arg2, arg3):
    my_list = []
    my_list.append(arg1)
    my_list.append(arg2)
    my_list.append(arg3)
    my_list.sort()
    print(f"Summ: {my_list[1] + my_list[2]}")


def my_fun_without_sort(arg1, arg2, arg3):
    if arg1 < arg2 and arg1 < arg3:
        print(f"Summ: {arg2 + arg3}")
    elif arg1 > arg2 and arg1 < arg3:
        print(f"Summ: {arg1 + arg3}")
    elif arg1 < arg2 and arg1 > arg3:
        print(f"Summ: {arg1 + arg2}")


arg1 = 3
arg2 = 8
arg3 = 6
my_fun_with_sort(arg1, arg2, arg3)
my_fun_without_sort(arg1, arg2, arg3)

