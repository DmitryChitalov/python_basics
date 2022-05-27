"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def my_func(a, b, c):
    if a > b and c > b:
        return a + c
    elif b > a and c > a:
        return b + c
    elif a > c and b > c:
        return a + b


print(my_func(1, 22, 3))


def func(a, b, c):
    my_list = []
    my_list.append(a)
    my_list.append(b)
    my_list.append(c)
    my_list.sort()
    return lis[-1] + lis[1]


def get_max(*args):
    print(sum(sorted(list(args), reverse=True)[:2]))

get_max(12,3,4)
