"""
Задание 4.

Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и только арифметические операции.
Не используйте взятие по индексу.

Пример:
Ведите целое положительное число: 123456789
Самая большая цифра в числе: 9
"""

"""
Выполение! Емельяненко А.А.
"""
number = int(input("Введите целое положительное число: "))
max_num = 0
while number != 0:
    cur_n = number % 10
    if max_num < cur_n:
        max_num = cur_n
    number = number // 10

print(f"Самая большая цифра в числе: {max_num}")
