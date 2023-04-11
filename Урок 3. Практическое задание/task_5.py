def my_str ():
    sum_str = 0
    ex = False
    while ex == False:
        number = input('Введите строку чисел через пробел или Q для выхода: ').split()

        res = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_str = sum_str + res
        print(f' Текущая сумма {sum_str}')
    print(f' Итоговая сумма {sum_str}')
my_str()
