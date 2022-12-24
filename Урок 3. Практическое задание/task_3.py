"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""

# c функицей sort
def my_func(*args):
    print(sum(sorted(list(args))[1:3]))

my_func(50, 10, 30)

# без функции sort
def my_func_2(*args):
    func = list(args)
    result = 0
    max_number = 0
    i = 0
    while i != 2:
        max_number = max(func)
        result += max_number
        func.remove(max_number)
        i += 1
    print(result)

my_func_2(50, 10, 30)
