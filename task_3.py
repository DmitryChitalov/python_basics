"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""
def my_func_sort(a, b, c):
    sp_tmp = [a, b, c]
    sp_tmp.sort()
    return sp_tmp[1] + sp_tmp[2]


def my_func(a, b, c):
    if a > b and a > c:
        if b > c:
            return a + b
        else:
            return a + c
    elif b > a and b > c:
        if a > c:
            return b + a
        else:
            return b + c
    else:
        if a > b:
            return c + a
        else:
            return c + b


a, b, c = map(int,input('Введите три числа через пробел: ' ).split())
print(f' используя сорт {my_func_sort(a, b, c)}')
print(f' не используя сорт {my_func(a, b, c)}')