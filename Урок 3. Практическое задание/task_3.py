"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def my_func(first, second, last):
    """info"""
    items = [first, second, last]
    items.remove(min(items))

    return sum(items)


a, b, c = int(input("Число a >>> ")), int(input("Число b >>> ")), int(input("Число c >>> "))

print(my_func(a, b, c))
