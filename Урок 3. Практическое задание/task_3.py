"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""

def sort_func(*vals):
    """Поиск суммы наибольших двух аргументов при помощи sort"""
    vals = list(vals)
    vals.sort(reverse=True)
    return vals[0] + vals[1]

def no_sort_func(*vals):
    """Поиск суммы наибольших двух аргументов без sort"""
    vals = list(vals)
    vals.remove(min(vals))
    return sum (vals)

a = int(input('Аргумент 1: '))
b = int(input('Аргумент 2: '))
c = int(input('Аргумент 3: '))

print(f'используя функцию sort(): {sort_func(a, b, c)}')
print(f'без функции sort(): {no_sort_func(a, b, c)}')
