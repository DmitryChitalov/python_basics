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
whole_number = int(input("Введите целое положительное число: "))
result_number = 0
while whole_number > result_number:
    search = whole_number % 10
    if search > result_number:
        result_number = search
    whole_number = whole_number // 10
print(f"Самая большая цифра в числе: {result_number}")
