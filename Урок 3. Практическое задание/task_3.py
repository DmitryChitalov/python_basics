"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def my_func_sort(a, b, c):
    num_lst = [a, b, c]
    num_lst.sort()
    return f'{num_lst[1]} {num_lst[2]}'


def my_func_without_sort(a, b, c):
    if a <= b and a <= c:
        return f'{b} {c}'
    elif b <= a and b <= c:
        return f'{a} {c}'
    return f'{a} {b}'


num1 = int(input('Введите целое число: '))
num2 = int(input('Введите целое число: '))
num3 = int(input('Введите целое число: '))

print(my_func_sort(num1, num2, num3))
print(my_func_without_sort(num1, num2, num3))
