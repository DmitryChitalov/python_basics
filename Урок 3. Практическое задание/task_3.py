"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""

"Без sort"


def my_func(arg1: int, arg2: int, arg3: int) -> object:
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg2 < arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3


def my_func_with_sort(arg1: int, arg2: int, arg3: int) -> int:
    args = [arg1, arg2, arg3]
    args.sort()
    return args[1] + args[2]


a1 = int(input("Введите 1 аргумент: "))
a2 = int(input("Введите 2 аргумент: "))
a3 = int(input("Введите 3 аргумент: "))

print(f'Result - {my_func(a1, a2, a3)}')
print(f'Result - {my_func_with_sort(a1, a2, a3)}')
