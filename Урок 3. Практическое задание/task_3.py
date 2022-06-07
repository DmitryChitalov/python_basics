"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""
def my_func(a, b, c):
    li = [a, b, c]
    li.sort()
    res = li[2] + li[1]

    lis = [a, b, c]
    for i in range(len(lis)-1, 0, -1):
        if lis[i] < lis[i-1]:
            lis[i-1], lis[i] = lis[i], lis[i-1]
    res2 = lis[2] + lis[1]

    print(res, res2, end='\n')

my_func(3, 9, 6)
my_func(1, 5, 2)
