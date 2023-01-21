"""
4. Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""
var_for_positive_integer = input("Введите целое положительное число: ")
largest_figure = var_for_positive_integer[0]
index = 0
while index < (len(var_for_positive_integer) - 1):
    largest_figure = max(largest_figure, var_for_positive_integer[index + 1])
    index = index + 1
print(f"Самая большая цифра в числе равна :{largest_figure}")
