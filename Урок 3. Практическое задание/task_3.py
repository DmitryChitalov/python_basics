"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""

# 1

def get_max(*args):
    print(sum(sorted(list(args), reverse=True)[:2]))

get_max(100, 1, 200)


# 2

def get_max(*args):
    lst = list(args)
    i = 0
    res = 0
    while i != 2:
        max_val = max(lst)
        res += max_val
        lst.remove(max_val)
        i += 1
    print(res)

get_max(100, 1, 200)
