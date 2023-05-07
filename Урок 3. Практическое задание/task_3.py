"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def my_func1(a, b, c):
    m = [a, b, c]
    m.sort()
    sum1 = m[-1] + m[-2]
    return sum1


def my_func2(d, e, f):
    n = [d, e, f]
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(n) - 1):
            if n[i] > n[i + 1]:
                n[i], n[i + 1] = n[i + 1], n[i]
                swapped = True
    sum2 = n[-1] + n[-2]
    return sum2


x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))
z = int(input('Введите третье число: '))
print(f"Сумма с использованием sort(): {my_func1(x, y, z)}")
print(f"Сумма без использованием sort(): {my_func2(x, y, z)}")
