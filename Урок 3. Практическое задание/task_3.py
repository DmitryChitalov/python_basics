"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def with_sort(a, b, c):
    return sum(sorted([a, b, c], reverse=True)[:2])


def without_sort(a, b, c):
    return max([a + b, a + c, b + c])


x, y, z = 1, 2, 3
print(f"используя функцию sort(): {with_sort(x, y, z)}, "
      f"без функции sort(): {without_sort(x, y, z)}")
