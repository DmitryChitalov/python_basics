# собираем целое число из отдельных цифр
n = int(input("Введите число N: "))
nn = [n, n]
nnn = [n, n, n]

number_from_nn = int(''.join((str(i) for i in nn)))
number_from_nnn = int(''.join((str(i) for i in nnn)))

print(f'Сумма n + nn + nnn: {n + number_from_nn + number_from_nnn}')
