f_char = open("DZ5_5.txt", 'w+')
f_char.write(input('Введите числа через пробел '))
f_char = open("DZ5_5.txt", 'r')
fin_sum = 0
for i in f_char:
    sum_list = i.split(' ')
    for el in sum_list:
        fin_sum += int(el)
print(f'Сумма введенных чисел равна {fin_sum}')
f_char.close()
