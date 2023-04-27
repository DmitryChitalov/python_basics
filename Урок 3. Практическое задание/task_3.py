"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""

def my_func(arg1 , arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 > arg2 and arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3

print(f'Result - {my_func(int(input("первый аргумент ")), int(input("второй аргумент ")), int(input("третий аргумент ")))}')

def my_func_srtd(arg4, arg5, arg6):
    return sum(map(lambda x : x, sorted((arg4, arg5, arg6))[1:]))

print(f'Result - {my_func_srtd(int(input("первый аргумент ")), int(input("второй аргумент ")), int(input("третий аргумент ")))}')
