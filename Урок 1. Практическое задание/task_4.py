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
maximal_number = 0
number = int(input("Введите число ->   "))
while number > 1:

    if number % 10 > maximal_number:
        maximal_number = number % 10
        number = number // 10
    else:
        number = number // 10  


print(maximal_number)