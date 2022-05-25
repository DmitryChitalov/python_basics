"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""


def check_for_number(num):
    try:
        if int(num) > 0:
            return True
        else:
            return False
    except:
        return False


while True:
    number = input('Введите число n ==>')
    if check_for_number(number):
        result = int(number) + int(number * 2) + int(number * 3)
        print(f'n + nn + nnn = {result}')
        break
    else:
        print('Введите целое положительное число...')
    
