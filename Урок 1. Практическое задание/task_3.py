"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
input_num = input('Укажите целое число n: ')

digit = len(str(input_num))
output_num_1 = int(input_num) * (10 ** (2 * digit) + 2 * (10 ** digit) + 3)
output_num_2 = int(input_num) + int(input_num + input_num) + int(input_num + input_num + input_num)

print('Результат вычисления (1) n + nn + nnn: ', output_num_1)
print('Результат вычисления (2) n + nn + nnn: ', output_num_2)