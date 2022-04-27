"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""

input_value = input("Please, input a integer value n=")
if str.isdigit(input_value):
    int_value = int(input_value)
    double_value = int_value * 2
    tripple_value = int_value * 3
    print(f"Result n + nn + nnn: {int_value}{double_value}{tripple_value}")
else:
    print("Error: your value is not a integer number")