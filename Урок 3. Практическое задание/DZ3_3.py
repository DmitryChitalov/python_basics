def my_func(a, b, c):
    my_list = [a, b, c]
    my_list.sort()
    my_sum = int(my_list[1]) + int(my_list[2])
    return print(f'Сумма двух наибольших элементов равна - {my_sum}')
my_func(input('Введите первое число: '), input('Введите второе число: '), input('Введите третье число: '))

#альтернативный способ решения

def my_func_alt(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    print(f'Сумма двух наибольших элементов равна - {a + b + c - min([a, b, c])}')
my_func_alt(input('Введите первое число: '), input('Введите второе число: '), input('Введите третье число: '))