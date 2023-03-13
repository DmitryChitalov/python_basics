"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""
def my_func(arg1, arg2, arg3):
    my_list = list([arg1, arg2, arg3])
    my_list.sort(reverse=True)
    return int(my_list[0]) + int(my_list[1])


def func_without_sort(arg1, arg2, arg3):
    result = arg1 + arg2 + arg3 - (min([arg1, arg2, arg3]))
    return result


a = int(input('Введите число 1: '))
b = int(input('Введите число 2: '))
c = int(input('Введите число 3: '))
print("Результат работы фнукции sort: ",my_func(a, b, c))
print("Без использования функции sort: ",func_without_sort(a, b, c))