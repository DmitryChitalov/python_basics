"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def my_func_with_sort(num_1, num_2, num_3):
    res_list = [num_1, num_2, num_3]
    res_list.sort()
    return res_list[1] + res_list[2]


def my_func(num_1, num_2, num_3):
    res_list = [num_1, num_2, num_3]
    res_list.remove(min(res_list))
    return sum(res_list)


n1 = int(input("Введите число 1: "))
n2 = int(input("Введите число 2: "))
n3 = int(input("Введите число 3: "))

print(my_func_with_sort(n1, n2, n3))
print(my_func(n1, n2, n3))
