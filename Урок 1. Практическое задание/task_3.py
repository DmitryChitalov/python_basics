"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
user_number = int(input("Введите число n: "))
print(f" {user_number} + {str(user_number) * 2} + {str(user_number) * 3} ")
print(f" {user_number + int(str(user_number) * 2) + int(str(user_number) * 3)}")