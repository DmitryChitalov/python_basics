def my_func(args_1, args_2, args_3):
    print(f'Сумма двух наибольших аргументов равна: {args_1 + args_2 + args_3 - min([args_1, args_2, args_3])}')
my_func(
    int(input('Аргумент 1:')),
    int(input('Аргумент 2:')),
    int(input('Аргумент 3:')),
)
