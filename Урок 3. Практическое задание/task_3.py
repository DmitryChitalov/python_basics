"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""

#1
def my_func(a, b, c):
    if a >= c and b >= c:
        return a + b
    elif a > b and a < c:
        return a + c
    else:
        return b + c
print(
    f'Сумму наибольших двух аргументов - {my_func(int(input("Введите первое значение ")), int(input("Введите второе значениее ")), int(input("Введите третье значение ")))}')

#2
def my_func_sort(arg_1, arg_2, arg_3):
    my_list = [arg_1, arg_2, arg_3]
    my_list.sort(reverse=True)
    result = my_list[0] + my_list[1]
    return result


arg_1, arg_2, arg_3 = [int(s) for s in input(f'Введите три числа '
                                             f'через пробел: ').split()]
print(
    f'Cумма больших двух чисел через сортировку {my_func_sort(arg_1, arg_2, arg_3)}')
