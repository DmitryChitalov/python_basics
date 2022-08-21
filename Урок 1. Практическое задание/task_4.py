n = int(input('Введите целое положительное число: '))
max_num = 0
while n > 0:
    if max_num < n % 10:
        max_num = n % 10
    n = n // 10
print(f'Самая большая цифра в числе: {max_num}')


