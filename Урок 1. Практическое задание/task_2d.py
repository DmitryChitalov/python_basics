"""
Задача 2: Найдите сумму цифр трехзначного числа.
"""

number = input('Введите трехзначное число: ')
sum = 0
if len(number) == 3:
    for i in number:
        sum += int(i)
    print(sum)
else:
    print('Вы ввели не 3-х значное число')
