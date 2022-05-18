"""
Задание 4.

Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и только арифметические операции.
Не используйте взятие по индексу.

Пример:
Ведите целое положительное число: 123456789
Самая большая цифра в числе: 9
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
        number = int(number)
        max_number = number % 10
        while number >= 1:
            number = number // 10
            if number % 10 > max_number:
                max_number = number % 10
            if number > 9:
                continue
            else:
                print(f'Максимальное число - {max_number}')
                break
        break
    else:
        print('Введите целое положительное число...')
