"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
inputed_value = int(input("Введите число n: "))

two_times_value = str(inputed_value) + str(inputed_value)
three_times_value = str(inputed_value) + str(inputed_value) + str(inputed_value)
c_sum = int(inputed_value) + int(two_times_value) + int(three_times_value)

"""
print(f'inputed_value = {inputed_value},\r\n '
      f'two_times_value = {two_times_value},\r\n '
      f'three_times_value = {three_times_value},\r\n '
      f'sum = {c_sum}')
"""
print(f'n + nn + nnn = {c_sum}')