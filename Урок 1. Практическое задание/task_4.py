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

integer_max = int(input("Введите целое положительное число: "))

max_element = integer_max % 10
integer_max = integer_max // 10
while integer_max > 0:
    if integer_max % 10 > max_element:
        max_element = integer_max % 10
    integer_max = integer_max // 10
print(f"Самая большая цифра в числе: {max_element}")
