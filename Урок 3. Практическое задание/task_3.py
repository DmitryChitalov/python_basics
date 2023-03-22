"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""

# Пользователь вводит 3 целых числа
user_int_1 = int(input('Введите первое число: '))
user_int_2 = int(input('Введите второе число: '))
user_int_3 = int(input('Введите третье число: '))


'''Функция записывает аргументы в список, сортирует данный список и выводит сложение максимальных значений'''
def my_func(*args):
    example_list = []

    for i in args:
        example_list.append(i)

    list_correct = sorted(example_list, reverse=True)
    return print(list_correct[0] + list_correct[1])


'''Функция записывает аргументы в список, выделяет 2 наибольших значения и выдает их сумму'''
def my_func_v2(*args):
    example_list = []
    f_num = 0
    s_num = 0

    for i in args:
        example_list.append(i)

    for i in example_list:
        if i > f_num:
            f_num = i

    for i in example_list:
        if i < f_num and i > s_num:
            s_num = i

    return print(f_num + s_num)


my_func(user_int_1, user_int_2, user_int_3)
my_func_v2(user_int_1, user_int_2, user_int_3)
