"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
time = int(input("Введите время в секундах: "))
hours = time / 3600
minutes = time / 60
print(f"Время в формате ч:м:с - {hours}: {minutes}: {time}")
