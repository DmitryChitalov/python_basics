"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
num = None
while not (isinstance(num, str) and num.isdigit()):
    num = input('Введите любимое число: ')

res = sum(map(int, [num, num*2, num*3]))
print(res)
