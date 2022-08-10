"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""
def my_func(num_1, num_2, num_3):
    res = []
    for i in (num_1, num_2, num_3):
        res.append(i)
    res.sort(reverse=True)
    print(res[0] + res[1])


def my_func_without_sort(num_1, num_2, num_3):
    res = []
    for i in (num_1, num_2, num_3):
        res.append(i)
    max_1 = res.pop(res.index(max(res)))
    max_2 = res.pop(res.index(max(res)))
    print(max_1 + max_2)


var_1 = float(input())
var_2 = float(input())
var_3 = float(input())
my_func(var_1, var_2, var_3)
my_func_without_sort(var_1, var_2, var_3)
