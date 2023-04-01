"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def my_func(list_x):
    sum = 0
    for i in range(0, 3):
        if i < 2:
            if list_x[i] < list_x[i + 1]:
                x = list_x[i]
                list_x[i] = list_x[i + 1]
                list_x[i + 1] = x
    for i in range(0, 2):
        sum += list_x[i]
    print(f"Сумма наибольших элементов равна: {sum}")


def my_func_s(list_x):
    list_x.sort(reverse=True)
    sum = 0
    for i in range(0, 2):
        sum += list_x[i]
    print(f"Сумма наибольших элементов равна: {sum}")


list_1 = [int(input("Введите число 1: ")), int(input("Введите число 2: ")), int(input("Введите число 3: "))]
print(list_1)
my_func(list_1)
my_func_s(list_1)
list_2 = list(map(int, input("Введите числа через пробел: ").split()))
print(list_2)
my_func(list_2)
my_func_s(list_2)