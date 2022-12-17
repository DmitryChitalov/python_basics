def my_funk(arg_1, arg_2):
    '''Функция формирует список четных чисел в диапазоне от arg_1 до arg_2
    и возвращает произведение всех элементов данного списка.'''
    my_list = [el for el in range(arg_1, (arg_2 + 1)) if el % 2 == 0]
    count = 1
    for i in range(1, len(my_list)):
        count = count * i
        i += 1
    return(count)

print(reduce(my_funk, [100, 1000]))