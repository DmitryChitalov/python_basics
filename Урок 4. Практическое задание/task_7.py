"""
7. Реализовать генератор с помощью функции с ключевым словом yield,
 создающим очередное значение.

 При вызове функции должен создаваться объект-генератор.
 Функция должна вызываться следующим образом: for el in fact(n).
 Функция отвечает за получение факториала числа,
 а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.

Подсказка: факториал числа n — произведение чисел от 1 до n.
Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""

from math import factorial


def fact_(x):
    a = 1
    b = 1
    if x == 0:
        a = 1
    if x < 0:
        print('Отрицательные не позволены!')
    if x > 0:
        while b <= x:
            a = a * b
            b += 1
            yield a


for el in fact_(4):
    print(el)


def fact(n):
    for el_ in range(1, n + 1):
        yield factorial(el_)


for el in fact(4):
    print(el)
