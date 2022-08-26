"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def my_func_sort(*a):
    b = list(a)
    b.sort(reverse=True)
    return b[0] + b[1]


def my_func(*a):
    total = 0
    minimum = 99999999
    for x in a:
        total += x
        minimum = x if minimum > x else minimum
    return total - minimum


number_list = 11, 2, 23

result_sort = my_func_sort(*number_list)
result = my_func(*number_list)

print(f"Результат с сортировкой: ", result_sort)
print(f"Результат без сортировки: ", result)
