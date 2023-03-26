"""
Задача 32: Определить индексы элементов списка, значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)
Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
Вывод: [1, 9, 13, 14, 19]
"""


from random import randint


class NewEx(Exception):
    pass


try:
    var_min, var_max = int(input("Введите нижнюю границу поиска элементов: ")), int(
        input("Введите верхнюю границу поиска элементов: "))
    if var_min == var_max or var_min > var_max:
        raise NewEx()
    list_a = []
    for i in range(1, 15):
        list_a.append(randint(-10, 50))
    print(list_a)
    list_b = []
    for i in range(len(list_a)):
        if list_a[i] < var_max and list_a[i] > var_min:
            list_b.append(list_a[i])
    print(list_b)
except ValueError:
    print("Ошибка ввода числа")
except NewEx:
    print("Задайте границы корректней")
