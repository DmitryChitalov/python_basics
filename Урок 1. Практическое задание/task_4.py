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
n = input('Ведите целое положительное число: ')
i = 0
max_n = 0
while i < len(n):
    if max_n < int(n[i]):
        max_n = int(n[i])
    i += 1

print(max_n)
