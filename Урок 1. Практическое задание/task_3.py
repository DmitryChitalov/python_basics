"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
#!/usr/bin/env python3
user_input = input("Пожалуйста, введите число n: ")
print(f"Нам с Питоном нужно подумать ... {user_input} + {user_input * 2} + {user_input * 3}")
print(f"Мы с Питоном посчитали, что n + nn + nnn будет: {int(user_input) + int(user_input * 2) + int(user_input * 3)}")
