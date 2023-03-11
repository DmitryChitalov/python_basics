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

num = int(input('Введите целое положительное число: '))
max_num = 0
while num > 0:
    if (num % 10) > max_num:
        max_num = num % 10
    num = int(num / 10)
print(f'Самая большая цифра в числе = {max_num}')
