"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def func_summ():
    value1 = int(input("Введите первое число: "))
    value2 = int(input("Введите второе число: "))
    value3 = int(input("Введите третье число: "))
    if value1 >= value2 and value1 >= value3:
        print(value1 + max(value2, value3))
    elif value2 >= value1 and value2 >= value3:
        print(value2 + max(value1, value3))
    else:
        print(value3 + max(value1, value2))


func_summ()
