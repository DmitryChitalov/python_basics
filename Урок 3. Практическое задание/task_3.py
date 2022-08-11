"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""
def my_func(a, b, c):
    return a + b + c - min(a, b, c)   # без функции sort()

print(my_func(15, 8, 10))


def my_func1(a, b, c):
    new_list = [a, b, c]
    new_list.sort() # с функцией sort()
    return new_list[1] + new_list[2]

print(my_func1(8, 1, 10))



