"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""

def my_func(a, b, c):
    my_list = [a, b, c]
    total = []
    my_list.sort()
    my_list.reverse()
    total.append(my_list[0])
    total.append(my_list[1])
    print(sum(total))
my_func(5, 9, 1)

def my_func_2(a, b, c):
    my_list = [a, b, c]
    total = []
    max_1 = max(my_list)
    total.append(max_1)
    my_list.remove(max_1)
    max_2 = max(my_list)
    total.append(max_2)
    print(sum(total))
my_func_2(5, 9, 1)
