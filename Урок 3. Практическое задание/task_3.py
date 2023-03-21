"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def my_func(var_1, var_2, var_3):
    temp = [var_1, var_2, var_3]
    temp.sort(reverse=1)
    return temp[0] + temp[1]


print(my_func(2, 1, 4))


def my_func(var_1, var_2, var_3):
    temp = [var_1, var_2, var_3]
    for i in range(len(temp) - 1):
        for j in range(0, len(temp) - i - 1):
            if temp[j] < temp[j + 1]:
                temp[j], temp[j + 1] = temp[j + 1], temp[j]
    return temp[0] + temp[1]


print(my_func(2, 1, 4))
