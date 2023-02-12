"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
usr_numb = input('Введите целое положительное число i \n')
term_1 = int(usr_numb)
term_2 = int(usr_numb + usr_numb)
term_3 = int(usr_numb + usr_numb + usr_numb)
total = term_1 + term_2 + term_3
print('Сумма i + ii + iii составляет:', total)