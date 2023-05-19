"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""

nubmer = input('Введите число: ')

second_number = nubmer+nubmer
third_number = nubmer+nubmer+nubmer

answer = int(nubmer) + int(second_number) + int(third_number)
print('Ответ: ', answer)
