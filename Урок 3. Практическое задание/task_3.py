"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""
def my_func(arg1, arg2, arg3):
    my_list = [arg1, arg2, arg3]
    res = []
    max1 = max(my_list)
    res.append(max1)
    my_list.remove(max1)
    max2 = max(my_list)
    res.append(max2)
    print(sum(res))


my_func(10, 5, 1)

