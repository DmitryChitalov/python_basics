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

n = int(input("Ведите целое положительное число: "))
m = 9
a = 0
while a < m:
    c = n
    while c > 0:
        a = int(c % 10)
        if a < m:
            c = int(c / 10)
        else:
            break
    m -= 1
print(a)
