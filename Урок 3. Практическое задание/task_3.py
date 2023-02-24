"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""

# 1) используя функцию sort()
def my_func(var_a, var_b, var_c):
    my_list = [var_a, var_b, var_c]
    my_list.sort()
    my_sum = int(my_list[1]) + int(my_list[2])
    return print(f'Сумма c функциtq sort() = {my_sum}')
my_func(input('Введите число #1: '), input(
    'Введите число #2: '), input('Введите число #3: '))

# 2) без функции sort()
def my_func_alt(var_a, var_b, var_c):
    var_a = int(var_a)
    var_b = int(var_b)
    var_c = int(var_c)
    print(f'Сумма без функции sort() = '
          f'{var_a + var_b + var_c - min([var_a, var_b, var_c])}')
my_func_alt(
    input('Введите число #1: '), input(
    'Введите число #2: '), input('Введите число #3: '))