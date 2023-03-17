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
#!/usr/bin/env python3
print("Способ 1")
user_input = input("Пожалуйста, введите целое положительное число: ")
print(max(user_input))

print("Способ 2")
user_input = int(input("Пожалуйста, введите целое положительное число: "))
search_iteration = user_input % 10
user_input = user_input // 10
while user_input > 0:
    if user_input % 10 > search_iteration:
        search_iteration = user_input % 10
    user_input = user_input // 10

print(search_iteration)
