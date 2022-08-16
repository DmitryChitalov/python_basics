"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""
def my_func_sort(a, b , c):
    '''сумма двух больших аргументов'''
    sort_list = [a, b, c]
    sort_list.sort(reverse=True)
    return sort_list[0] + sort_list[1]
def my_func(a, b , c):
    '''сумма двух больших аргументов без sort'''
    vals_list = [a, b, c]
    vals_list.remove(min(vals_list))
    return vals_list[0] + vals_list[1]
try:
    val_1 = int(input('Введите число 1: '))
    val_2 = int(input('Введите число 2: '))
    val_3 = int(input('Введите число 3: '))
except ValueError:
    print('Одно из введенных чисел не является числом')
print(f'Сумма с sort: {my_func_sort(val_1, val_2, val_3)}')
print(f'Сумма без sort: {my_func_sort(val_1, val_2, val_3)}')
