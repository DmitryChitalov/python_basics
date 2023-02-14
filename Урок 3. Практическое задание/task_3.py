"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""

Без функции sort()


def my_func(argument1, argument2, argument3):
    print(f'Сумма двух наибольших аргументов равна: {argument1 + argument2 + argument3 - min([argument1, argument2, argument3])}')


my_func(
    int(input('Аргумент 1:')),
    int(input('Аргумент 2:')),
    int(input('Аргумент 3:')),
)