user_int = int(input('Введите целое положительное число: '))

big_number = 0
while user_int > 1:
    d = user_input % 10
    user_int = user_int // 10
    if d > big_number:
        big_number = d

print(f'Самая большая цифра в числе: {big_number}')
