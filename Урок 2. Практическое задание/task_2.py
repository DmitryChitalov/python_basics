"""
Задание 2. Для списка реализовать обмен значений соседних элементов,
т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().

Пример:
Введите целые числа через пробел: 1 2 3 4
Результат: 2 1 4 3

Введите целые числа через пробел: 1 2 3
Результат: 2 1 3
"""
#!/usr/bin/env python3
user_input = input("Пожалуйста, введите целые числа через пробел: ")
user_list = user_input.split()

if len(user_list) % 2 == 0:
    print("Вы ввели чётное количество чисел.")
    for i in range(0, len(user_list), 2):
        user_list[i], user_list[i + 1] = user_list[i + 1], user_list[i]
    print(f"Результат: {user_list}.")
else:
    last_odd_number = user_list[-1]
    print(f"Вы ввели нечётное количество чисел. Последнее число в списке: {last_odd_number}")
    for i in range(0, len(user_list) - 1, 2):
        user_list[i], user_list[i + 1] = user_list[i + 1], user_list[i]
    print(f"Результат: {user_list}.")
