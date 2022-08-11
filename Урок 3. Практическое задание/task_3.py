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


arg1 = int(input('Первое значение : '))
arg2 = int(input('Второе значение: '))
arg3 = int(input('Третие значение: '))
print(f"Сумма наибольших значений с функцией sort(): {my_func_with_sort(arg1, arg2, arg3)}")
print(f"Сумма наибольших значений без функции sort(): {my_func_without_sort(arg1, arg2, arg3)}")
