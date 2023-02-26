"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""

#sort
def max_num(*args):
    print(sum(sorted(list(args), reverse=True)[:2]))
max_num(40, 60, 150)

#no_sort
def max_num(*args):
    lst = list(args)
    n = 0
    result = 0
    while n != 2:
        max_val = max(lst)
        result += max_val
        lst.remove(max_val)
        n += 1
    print(result)
max_num(40, 60, 150)
