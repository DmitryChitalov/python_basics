"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""

def my_func_without_sort(val1, val2, val3):
    return val1 + val2 + val3 - min(val1, val2, val3)


def my_func_with_sort(val1, val2, val3):
    my_list = [val1, val2, val3]
    my_list.sort()
    return my_list[1] + my_list[2]


arg1 = int(input('input first arg: '))
arg2 = int(input('input second arg: '))
arg3 = int(input('input third arg: '))
print(f"result with func sort(): {my_func_with_sort(arg1, arg2, arg3)}")
print(f"result without func sort(): {my_func_without_sort(arg1, arg2, arg3)}")