def my_func(my_sum=0):
    num = input('Введите числа через пробел: ').split()
    for el in range(len(num)):
        if num[el] != 'stop':
            my_sum = my_sum + int(num[el])
        else:
            break
    print(my_sum)
    if 'stop' in num:
        exit('Выход из программы')
    else:
        my_func(my_sum)

my_func()