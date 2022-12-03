"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def my_func1(a, b, c):
    my_array = sorted([float(a), float(b), float(c)])
    return my_array[-1] + my_array[-2]


def my_func2(a, b, c):
    a = float(a)
    b = float(b)
    c = float(c)
    big = min(a, b, c)
    return (a + b + c) - big


print(my_func1(10, 20, "30"))
print(my_func2(10, 20, "30"))
