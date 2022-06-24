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
print("Задание №4")
max_number = int(input("Введите число "))
divider = 10
number_1 = 0
while max_number > 0:
    number = int(max_number % divider)
    maxcheslo = int((max_number - number) / divider)
    if number >= number_1:
        number_1 = number
print(f"{number_1}")
