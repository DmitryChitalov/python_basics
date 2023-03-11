def my_func(a, b, c):  # Вариант 1
    d = [a, b, c]
    d.sort()
    e = int(d[1]) + int(d[2])
    print(e)


my_func(a=input("Введите число"), b=input("Введите число"), c=input("Введите число"))


def my_func1(a, b, c):  # Вариант 2
    if b >= a <= c:
        e = int(b) + int(c)
        print(e)

    if a >= b <= c:
        e = int(a) + int(c)
        print(e)

    if a >= c <= b:
        e = int(a) + int(b)
        print(e)


my_func1(a=input("Введите число"), b=input("Введите число"), c=input("Введите число"))

"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""
