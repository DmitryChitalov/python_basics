"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
point = int(input("Введите число:"))
numb1 = str(point)
numb2 = numb1 + numb1
numb3 = numb1 + numb1 + numb1
total = point + int(numb2) + int(numb3)
print(f"Результат: {total}")