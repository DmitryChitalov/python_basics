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
numb = int(input('input your digital:'))
max_dig = 0
while max_dig != 0:
    current_n = numb % 10
    if max_dig < current_n:
        max_dig = current_n
numb = numb // 10
print(f'Max huge digital:{max_dig}')
