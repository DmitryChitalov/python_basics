"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def my_func_1(a, b, c):
    if a < b:
        min = a
    else:
        min = b
    if c < min:
        min = c
    s = a + b + c - min
    print("1) без функции sort(), сумма двух наибольших чисел = ", s)


def my_func_2(*args):
    sum_max = list(args)
    sum_max.sort()
    sum = sum_max[1] + sum_max[2]
    print("2) используя функцию sort(), сумма двух наибольших чисел = ", sum)


a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
my_func_1(a, b, c)
my_func_2(a, b, c)