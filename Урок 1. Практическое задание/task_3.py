number = input('Введите положительное число:')
if number.isdigit():
    print(max(sorted(map(int, str(number)))))
else:
    print('Сказали: число!')
