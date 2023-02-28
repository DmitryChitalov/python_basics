"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""
a = int(input('Введите число 1: '))
b = int(input('Введите число 2: '))
c = int(input('Введите число 3: '))

def my_func_sort(a1, a2, a3):
    summ = list([a1, a2, a3])
    summ.sort(reverse=True)
    return int(summ[0]) + int(summ[1])


def my_func_wsort(a1, a2, a3):
    summ = a1 + a2 + a3 - (min([a1, a2, a3]))
    return summ

print("С фнукцией sort: ", my_func_sort(a, b, c))
print("Без функции sort: ", my_func_wsort(a, b, c))