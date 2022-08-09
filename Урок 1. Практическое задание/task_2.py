number = int(input('Введите число:'))
two_number = int(f'{number}{number}')
three_number = int(f'{two_number}{number}')
print(number + two_number + three_number)
