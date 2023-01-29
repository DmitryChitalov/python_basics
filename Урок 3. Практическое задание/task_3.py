"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""

def my_func(arg_1, arg_2, arg_3):
    my_list = [arg_1, arg_2, arg_3]
    my_list.sort()
    return my_list[2] + my_list[1]

my_sum = my_func(6, 777, 59)
print(f'Сумма с использованием функции sort: {my_sum}')

def my_func_no_sort(one, two, free):
    my_list = [arg_1, arg_2, arg_3]
    my_list.remove(min(my_list))
    return sum(list_args)

my_sum = my_func_no_sort(6, 777, 59)
print(f'Сумма без функции sort: {my_sum}')
