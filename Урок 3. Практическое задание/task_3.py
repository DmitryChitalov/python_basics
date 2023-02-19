"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""

"""Вычисление с соритровкой"""


def my_func(num1, num2, num3):
    try:
        spot = int[num1, num2, num3]
        spot.sort(reverse=True)
        return spot[0] + spot[1]
    except TypeError:
        return 'Ошибка!Вводите только числа'


print(
    f'Result - {my_func(input("Введите первое значение "), input("Введит второе значение "), input("Введите третье значение "))}')

"""Вычисление без сортировки"""


def my_func(n1, n2, n3):
    if n1 >= n3 and n2 >= n3:
        return n1 + n2
    elif n1 > n2 and n1 < n3:
        return n1 + n3
    else:
        return n2 + n3


print(
    f'Result - {my_func(int(input("Введите первое значение ")), int(input("Введит второе значение ")), int(input("Введите третье значение ")))}')
