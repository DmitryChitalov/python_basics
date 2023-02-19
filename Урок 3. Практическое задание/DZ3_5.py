def sum_func():
    save_sum = 0
    my_exit = False
    while my_exit == False:
        my_list = input('Введите числа через пробел, для выхона введите ! ').split(' ')
        tmp_sum = 0
        for el in range(len(my_list)):
            if my_list[el] == "!":
                my_exit = True
            else:
                tmp_sum = tmp_sum + int(my_list[el])
        save_sum = save_sum + tmp_sum
        print(f'Общая сумма чисел равна: {save_sum}, сумма последних чисел равна {tmp_sum}')
    return
sum_func()