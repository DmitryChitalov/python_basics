"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
ent_number = input('Введите челое положительное число :')
first_num = int(ent_number)
second_num = int(ent_number + ent_number)
third_num = int(ent_number * 3)

print("n + nn + nnn = ", first_num + second_num + third_num)



