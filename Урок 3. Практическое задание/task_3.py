"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


# Вариант 1
def my_func(*args):
    print(sum(sorted(list(args), reverse=True)[:2]))


my_func(70, 20, 30)


# Вариант 2
def my_func(*args):
    lst = list(args)
    i = 0
    res = 0
    while i != 2:
        max_val = max(lst)
        res += max_val
        lst.remove(max_val)
        i += 1
    print(res)


my_func(10, 20, 30)
