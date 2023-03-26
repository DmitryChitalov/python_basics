
"""
Задача 30: Заполните массив элементами арифметической
прогрессии. Её первый элемент, разность и количество
элементов нужно ввести с клавиатуры. Формула для
получения n-го члена прогрессии: an= a1+ (n-1) * d.
Каждое число вводится с новой строки.
Ввод: 7 2 5
Вывод: 7 9 11 13 15
"""


class NewEx(Exception):
    pass


try:
    var_first, var_diff, var_sum = int(input("Введите первый элемент списка: ")), int(
        input("Введите шаг списка: ")), int(input("Введите количество элемент списка: "))
    if var_diff < 1 or var_sum < 1:
        raise NewEx
    list_1, count = [], 1
    for i in range(var_first, var_sum * var_diff + var_first):
        if i == var_first:
            list_1.append(i)
        elif i == var_first + var_diff * count:
            list_1.append(i)
            count += 1
    print(*list_1)
except ValueError:
    print("Введите числа")
except NewEx:
    print("Введите положительные значения шага и/или количества элементов массива")
