"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
#!/usr/bin/env python3
user_input = int(input("Пожалуйста, введите число n: "))
print(f"Нам с Питоном нужно подумать ... {user_input} + {str(user_input) * 2} + {str(user_input) * 3} ...")
print(f"Мы с Питоном посчитали, что n + nn + nnn будет: {user_input + int(str(user_input) * 2) + int(str(user_input) * 3)}")
