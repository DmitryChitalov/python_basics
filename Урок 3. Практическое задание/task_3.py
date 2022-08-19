"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def my_func_sort(var_a, var_b, var_c):
    lst = []
    for i in (var_a, var_b, var_c):
        lst.append(i)
    lst.sort(reverse=True)
    return lst[0] + lst[1]


def my_func(var_a, var_b, var_c):
    return var_a + var_b + var_c - min(var_a, var_b, var_c)


a = 3
b = 4
c = 5
print(f"Аргументы: {a} {b} {c}")
print(f"Результат с сорт: {my_func_sort(a, b, c)}")
print(f"Результат перебор: {my_func(a, b, c)}")
