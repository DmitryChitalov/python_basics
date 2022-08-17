"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""

def my_func(arg1, arg2, arg3):
    if arg1 >= arg2 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 >= arg2 and arg3 >= arg2:
        return arg1 + arg3
    elif arg2 >= arg1 and arg3 >= arg2:
        return arg2 + arg3
    elif arg2 >= arg1 and arg2 >= arg3:
        return arg2 + arg1

print(my_func(4, 6, 3))
def my_func2(arg4, arg5, arg6):
    list1 = [arg4, arg5, arg6]
    list1.sort(reverse=True)
    return list1[0] + list1[1]

print(my_func2(4, 6, 3))