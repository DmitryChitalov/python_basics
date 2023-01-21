"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""

num = int(input("Введите число от 0 до 9: "))

# проверка введеного числа
if num == 0:
    result = 0
elif num > 9:
    result = "Вы ввели число больше 9"

# вычисление суммы
else:
    num_num = num * 10 + num
    num_num_num = num_num * 10 + num
    result = num + num_num + num_num_num

# вывод результата
print(result)
