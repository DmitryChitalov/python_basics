"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def my_func(one, two, free):
    my_list = [one, two, free]
    my_list.sort()
    return my_list[-1] + my_list[-2]


def my_func_2(one, two, free):
    my_list = [one, two, free]
    i = 1
    while i > 0:
        for k in range(len(my_list) - 1):
            i = 0
            if my_list[k] > my_list[k + 1]:
                my_list[k], my_list[k + 1] = my_list[k + 1], my_list[k]
                i += 1
    return my_list[-1] + my_list[-2]


my_sum = my_func(99, 123, 2)
print(f'Сумма посчитана с использованием функции sort: {my_sum}')
my_sum = my_func_2(99, 123, 2)
print(f'Сумма посчитана без функции sort: {my_sum}')
