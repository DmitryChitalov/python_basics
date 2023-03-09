"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""
a = 5
b = 8
c = 4


def sort_fn(_a, _b, _c):
    arr = [_a, _b, _c]
    arr.sort(reverse=True)
    print(arr[0], arr[1])


sort_fn(a, b, c)


def not_sort_fn(_a, _b, _c):
    arr = [_a, _b, _c]
    max_x = max(arr)
    arr.remove(max_x)
    max_y = max(arr)
    print(max_x, max_y)


not_sort_fn(a, b, c)
