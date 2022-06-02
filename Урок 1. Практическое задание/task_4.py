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
n = int(input('Ведите целое положительное число: '))

max_n = n % 10

while n >= 1:
    n = n // 10
    if n % 10 > max_n:
        max_n = n % 10
    if n > 9:
        continue
    else:
        print(f'Самая большая цифра в числе: {max_n}')
        break
