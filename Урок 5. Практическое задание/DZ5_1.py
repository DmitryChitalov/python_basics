f_obj = open("DZ5_1.txt", 'w+')
while True:
    my_list = input('Введите данные, для выхона введите пустую строку ')
    if my_list == '':
        break
    else:
        f_obj.write(my_list + '\n')
f_obj.close()