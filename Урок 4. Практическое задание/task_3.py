"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""

def my_func(*args):
    my_lst = list(args)
    my_lst.sort()
    result = my_lst[1]+my_lst[2]
    return result

print(my_func(88,9,100))


def my_func(*args):
    args_list = list(args)
    max_num1 = max(args_list)
    args_list.remove(max_num1)
    max_num2 = max(args_list)
    result = max_num1 + max_num2
    return result

print(my_func(12,1,12))