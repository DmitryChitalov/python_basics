"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""



def my_func_hard(arg_1, arg_2, arg_3):
    if arg_1 >= arg_2 and arg_1 >= arg_3:
        if (arg_2 > arg_3):
            result = arg_1 + arg_2
        else:
            result = arg_1 + arg_3
    if arg_2 >= arg_1 and arg_2 >= arg_3:
        if (arg_1 > arg_3):
            result = arg_1 + arg_2
        else:
            result = arg_2 + arg_3
    if arg_3 > arg_1 and arg_3 > arg_2:
        if (arg_2 > arg_1):
            result = arg_3 + arg_2
        else:
            result = arg_1 + arg_3
    return result

def my_func_sort(arg_1, arg_2, arg_3):
    my_list = [arg_1, arg_2, arg_3]
    my_list.sort(reverse=True)
    result_2 = my_list[0] + my_list[1]
    return result_2

arg_1, arg_2, arg_3 = [int(s) for s in input(f'Введите три числа '
                                             f'через пробел: ').split()]
result_1 = my_func_hard(arg_1, arg_2, arg_3)
print(f'Сумма двух больших чисел: {result_1}')
print(f'Cумма больших двух чисел через сорти'
      f'ровку {my_func_sort(arg_1, arg_2, arg_3)}')

