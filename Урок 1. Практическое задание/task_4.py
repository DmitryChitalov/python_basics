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
n = int(input("Please enter number (n): "))
max_num = 0
while n > 0:
    print("Your number: ", n)
    n1 = n % 10
    #    print("первая цифра справа: ", n1)
    if n1 == 9:
        max_num = n1
        break
    elif n1 > max_num:
        max_num = n1
    n = n // 10
print("maximim digit in your number is: ", max_num)